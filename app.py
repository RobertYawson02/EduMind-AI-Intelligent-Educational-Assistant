import os
import secrets
from uuid import uuid4

from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from time import perf_counter
from werkzeug.security import check_password_hash

from model.qa_engine import process_question
from model.conversation_engine import clear_conversation
from model.web_engine import search_educational_web


# ==========================================================
# FLASK APPLICATION
# Intelligent Educational Assistant
# ==========================================================

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.getenv("SECRET_KEY", "local-development-only-change-me"),
    MAX_CONTENT_LENGTH=int(os.getenv("MAX_CONTENT_LENGTH", "32768")),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("SESSION_COOKIE_SECURE", "0").lower() in {"1", "true", "yes"},
)


def authentication_enabled():
    return os.getenv("AUTH_ENABLED", "0").lower() in {"1", "true", "yes"}


def credentials_are_valid(username, password):
    expected_username = os.getenv("APP_USERNAME", "supervisor")
    password_hash = os.getenv("APP_PASSWORD_HASH", "")
    if password_hash:
        return username == expected_username and check_password_hash(password_hash, password)
    expected_password = os.getenv("APP_PASSWORD", "")
    return username == expected_username and bool(expected_password) and secrets.compare_digest(
        password, expected_password
    )


@app.before_request
def ensure_session_identity():
    """Give each browser an opaque conversation identity."""
    if request.endpoint in {"health", "login", "static"}:
        return None
    if authentication_enabled() and not session.get("authenticated"):
        if request.path.startswith(("/ask", "/chat", "/search", "/conversation", "/clear", "/semantic")):
            return jsonify({"error": "Authentication required", "status": "unauthorized"}), 401
        return redirect(url_for("login", next=request.full_path))
    if "conversation_id" not in session:
        session["conversation_id"] = uuid4().hex
    return None


def current_conversation_id():
    return session.get("conversation_id", "anonymous")


@app.route("/login", methods=["GET", "POST"])
def login():
    if not authentication_enabled():
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if credentials_are_valid(username, password):
            session.clear()
            session["authenticated"] = True
            session["conversation_id"] = uuid4().hex
            next_url = request.args.get("next") or url_for("home")
            if not next_url.startswith("/") or next_url.startswith("//"):
                next_url = url_for("home")
            return redirect(next_url)
        return render_template("login.html", error="Invalid username or password."), 401
    return render_template("login.html", error="")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login")) if authentication_enabled() else redirect(url_for("home"))


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")



# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.route("/health", methods=["GET"])
def health():
    """Lightweight health endpoint for deployment and validation."""
    try:
        from model.knowledge_engine import knowledge_base
        knowledge_records = len(knowledge_base)
    except Exception:
        knowledge_records = 0

    return jsonify({
        "status": "ok",
        "service": "Intelligent Educational Assistant",
        "knowledge_records": knowledge_records,
        "capabilities": ["local_knowledge", "web_retrieval", "akan_twi", "conversation_memory"],
    }), 200


# ==========================================================
# ASK QUESTION
# ==========================================================

@app.route("/ask", methods=["POST"])
def ask():

    try:

        # Get JSON data from frontend
        data = request.get_json(silent=True)

        if not data:

            return jsonify({

                "answer": "Please send a valid question.",

                "source": "⚠️ System",

                "language": "unknown"

            }), 400


        # Extract question
        question = data.get(
            "question",
            ""
        ).strip()


        # Validate question
        if not question:

            return jsonify({

                "answer": "Please enter a question.",

                "source": "⚠️ System",

                "language": "unknown"

            }), 400


        # Send the question through the integrated QA pipeline.
        started = perf_counter()
        response = process_question(question)
        answer = response["answer"]
        source = response["source"]


        # Language detection for frontend
        language = "english"

        lower_question = question.lower()


        akan_characters = [
            "ɔ",
            "ɛ"
        ]


        akan_words = [

            "nsuo",
            "ɔdɔ",
            "meda ase",
            "maakye",
            "maaha",
            "maadwo",
            "akwaaba",
            "nante yie",
            "wo ho te sɛn",
            "me ho yɛ",
            "yɛn",
            "asɛm",
            "sukuu",
            "akan",
            "twi"

        ]


        if any(
            character in lower_question
            for character in akan_characters
        ):

            language = "akan"


        else:

            words = lower_question.split()


            for phrase in akan_words:

                if " " in phrase:

                    if phrase in lower_question:

                        language = "akan"

                        break

                else:

                    if phrase in words:

                        language = "akan"

                        break


        # Return response to frontend
        return jsonify({

            "answer": answer,

            "source": source,

            "sources": response.get("sources", []),

            "intent": response.get("intent", "general"),

            "topic": response.get("topic", ""),

            "confidence": response.get("confidence", 0.0),

            "language": response.get("language", language),

            "response_time_ms": round((perf_counter() - started) * 1000, 1),
            "status": "success"

        })


    except Exception:


        return jsonify({

            "answer":
                "An unexpected error occurred while processing your question.",

            "source":
                "⚠️ System",

            "language":
                "unknown",

            "status":
                "error"

        }), 500


@app.route("/search", methods=["GET", "POST"])
def search():
    """Return transparent, ranked web evidence for the research view."""
    data = request.get_json(silent=True) or {}
    query = request.args.get("q", data.get("query", "")).strip()
    if not query:
        return jsonify({"error": "A search query is required.", "results": []}), 400
    if len(query) > 300:
        return jsonify({"error": "Search query is too long.", "results": []}), 400

    try:
        results = search_educational_web(query)[:6]
        return jsonify({"query": query, "results": results, "status": "success"})
    except Exception:
        return jsonify({"query": query, "results": [], "status": "degraded"}), 200


# ==========================================================
# CONVERSATION RESET
# ==========================================================

# ==========================================================
# ENHANCED CONVERSATIONAL ENDPOINTS
# ChatGPT-like multi-turn dialogue
# ==========================================================

@app.route("/chat", methods=["POST"])
def chat():
    """
    Enhanced conversational endpoint with context awareness.
    Supports multi-turn dialogue like ChatGPT.
    """
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Invalid request"}), 400
        
        question = data.get("question", "").strip()
        if not question:
            return jsonify({"error": "Question required"}), 400
        
        from model.enhanced_conversation_engine import process_question_with_context
        from model.semantic_engine import get_complexity_level
        
        started = perf_counter()
        response = process_question_with_context(question, current_conversation_id())
        elapsed_ms = round((perf_counter() - started) * 1000, 1)
        
        # Calculate answer quality
        answer_quality = 0.85  # Default
        if response.get("confidence"):
            answer_quality = response["confidence"]
        
        return jsonify({
            "answer": response.get("answer", ""),
            "intent": response.get("intent", "general"),
            "topic": response.get("topic", ""),
            "language": response.get("language", "english"),
            "confidence": response.get("confidence", 0.75),
            "sources": response.get("sources", []),
            "is_followup": response.get("is_followup", False),
            "entities_mentioned": response.get("entities_mentioned", []),
            "follow_up_questions": response.get("follow_up_questions", []),
            "conversation_context": response.get("conversation_context", ""),
            "answer_quality": answer_quality,
            "response_time_ms": elapsed_ms,
            "status": "success"
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


@app.route("/conversation-history", methods=["GET"])
def conversation_history():
    """Get the conversation history."""
    try:
        from model.enhanced_conversation_engine import get_conversation_history
        history = get_conversation_history(current_conversation_id())
        return jsonify({
            "turns": history,
            "count": len(history),
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


@app.route("/conversation-stats", methods=["GET"])
def conversation_stats():
    """Get conversation statistics."""
    try:
        from model.enhanced_conversation_engine import get_conversation_stats
        stats = get_conversation_stats(current_conversation_id())
        return jsonify({
            "stats": stats,
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


@app.route("/clear-context", methods=["POST"])
def clear_context():
    """Clear enhanced conversation context (like ChatGPT 'new chat')."""
    try:
        from model.enhanced_conversation_engine import clear_enhanced_conversation
        clear_enhanced_conversation(current_conversation_id())
        return jsonify({"status": "success", "message": "Context cleared"}), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


@app.route("/semantic-analysis", methods=["POST"])
def semantic_analysis():
    """Analyze text semantically."""
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Invalid request"}), 400
        
        text = data.get("text", "").strip()
        if not text:
            return jsonify({"error": "Text required"}), 400
        
        from model.semantic_engine import (
            extract_concepts,
            understand_intent,
            get_complexity_level,
        )
        
        concepts = extract_concepts(text)
        intent_scores = understand_intent(text)
        complexity = get_complexity_level(text)
        
        # Determine primary intent
        primary_intent = max(intent_scores.items(), key=lambda x: x[1])[0] if intent_scores else "general"
        
        return jsonify({
            "text": text,
            "key_concepts": concepts,
            "intent": primary_intent,
            "intent_scores": intent_scores,
            "complexity_level": complexity,
            "status": "success"
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


# ==========================================================
# CONVERSATION RESET
# ==========================================================

@app.route("/clear-conversation", methods=["POST"])
def clear_conversation_route():
    """Clear persisted context used for follow-up questions."""
    if clear_conversation():
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 500



# ==========================================================
# APPLICATION START
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0").lower() in {"1", "true", "yes"},
    )
