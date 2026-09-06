"""Local educational knowledge retrieval.

The knowledge base is intentionally controlled and educational.  Retrieval uses
TF-IDF/cosine similarity over topic, keywords, definition, explanation,
examples, and category so the assistant can answer a wider range of academic
questions without relying entirely on live web search.
"""

import json
import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_PATH = os.path.join(BASE_DIR, "data", "educational_knowledge.json")
SYNONYMS_PATH = os.path.join(BASE_DIR, "data", "synonyms.json")


def _load_json_list(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except Exception as exc:
        print(f"Knowledge data load error [{path}]: {exc}")
        return []


def load_knowledge():
    data = _load_json_list(KNOWLEDGE_PATH)
    print(f"Knowledge Base Loaded: {len(data)} entries")
    return data


def _load_synonyms():
    try:
        with open(SYNONYMS_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


knowledge_base = load_knowledge()
synonyms = _load_synonyms()


def _flatten(value):
    if isinstance(value, list):
        return " ".join(str(x) for x in value if x)
    return str(value or "")


def _search_document(item):
    return " ".join([
        _flatten(item.get("topic")),
        _flatten(item.get("keywords")),
        _flatten(item.get("definition")),
        _flatten(item.get("explanation")),
        _flatten(item.get("examples")),
        _flatten(item.get("category")),
        _flatten(item.get("related_topics")),
    ]).strip()


documents = [_search_document(item) for item in knowledge_base if isinstance(item, dict)]
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    sublinear_tf=True,
    max_features=30000,
)
knowledge_vectors = None

if documents:
    try:
        knowledge_vectors = vectorizer.fit_transform(documents)
        print("Knowledge Search Index Ready.")
    except Exception as exc:
        print(f"Knowledge vectorization error: {exc}")


def _expand_query(question):
    q = str(question or "").strip().lower()
    if not q:
        return ""
    additions = []
    for key, values in synonyms.items():
        if key in q:
            if isinstance(values, list):
                additions.extend(str(v) for v in values[:5])
            elif values:
                additions.append(str(values))
    return " ".join([q, *additions])


def search_knowledge(question, min_similarity=0.16):
    if not question or not knowledge_base or knowledge_vectors is None:
        return None

    try:
        query = _expand_query(question)
        query_vector = vectorizer.transform([query])
        scores = cosine_similarity(query_vector, knowledge_vectors)[0]

        # Combine lexical intent with TF-IDF. Exact topic/keyword matches are
        # deliberately strong so a generic topic such as "Natural Language
        # Query" cannot outrank a direct match such as "Artificial Intelligence".
        q_lower = query.lower()
        q_tokens = set(re.findall(r"[a-zA-ZÀ-ÿɔɛƆƐ0-9]+", q_lower))
        combined = []
        for index, base_score in enumerate(scores):
            item = knowledge_base[index]
            topic = str(item.get("topic", "")).strip().lower()
            keywords = [str(x).strip().lower() for x in item.get("keywords", []) if x]
            lexical = 0.0
            if topic and topic in q_lower:
                lexical += 0.65
            for keyword in keywords:
                if keyword and keyword in q_lower:
                    lexical += 0.20
            topic_tokens = set(re.findall(r"[a-zA-ZÀ-ÿɔɛƆƐ0-9]+", topic))
            overlap = len(q_tokens & topic_tokens) / max(1, len(topic_tokens))
            lexical += min(0.20, overlap * 0.20)

            # Prefer the canonical definition record for definition-style
            # questions over broad topic variants such as "- Steps".
            definition_query = q_lower.startswith((
                "what is ", "what are ", "define ", "definition of ",
                "meaning of ",
            ))
            if definition_query:
                if topic.endswith((" - definition", " - meaning")):
                    lexical += 0.45
                elif " - " in topic and not topic.endswith((" - explanation", " - description")):
                    lexical -= 0.12
            combined.append(min(1.0, float(base_score) * 0.45 + lexical * 0.55))

        best_index = max(range(len(combined)), key=combined.__getitem__)
        best_score = float(combined[best_index])

        if best_score < min_similarity:
            return None

        result = dict(knowledge_base[best_index])
        result["retrieval_score"] = round(best_score, 4)
        return result
    except Exception as exc:
        print(f"Knowledge search error: {exc}")
        return None


def format_knowledge(result):
    if not isinstance(result, dict):
        return ""

    topic = str(result.get("topic", "")).strip()
    definition = str(result.get("definition", "")).strip()
    explanation = str(result.get("explanation", "")).strip()
    examples = result.get("examples", [])
    category = str(result.get("category", "")).strip()

    parts = []
    if definition:
        parts.append(definition)
    if explanation and explanation.lower() not in " ".join(parts).lower():
        parts.append(explanation)
    if examples:
        example_text = ", ".join(str(x) for x in examples if x)
        if example_text:
            parts.append(f"Examples include {example_text}.")
    return " ".join(parts).strip()


if __name__ == "__main__":
    for question in [
        "What is artificial intelligence?",
        "What are the applications of artificial intelligence?",
        "Explain machine learning",
        "What is DNS?",
        "What is cybersecurity?",
    ]:
        result = search_knowledge(question)
        print("\nQUESTION:", question)
        print("RESULT:", format_knowledge(result) if result else None)
