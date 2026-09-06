# ==========================================================
# RESPONSE ENGINE
# Intelligent Educational Response Generator
# ==========================================================

from datetime import datetime


# ==========================================================
# FOLLOW-UP QUESTION GENERATOR
# ==========================================================

def generate_follow_up(
    intent,
    language
):

    # ------------------------------------------------------
    # Akan
    # ------------------------------------------------------

    if language == "akan":

        return [

            "Translate another word.",
            "Use this word in a sentence.",
            "Show related Akan words.",
            "Explain the meaning further."

        ]


    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if intent == "definition":

        return [

            "Give an example.",
            "Explain it simply.",
            "Why is it important?",
            "Where is it used?"

        ]


    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    if intent == "explanation":

        return [

            "Can you explain further?",
            "Give a real-life example.",
            "What are the advantages?",
            "What are the disadvantages?"

        ]


    # ------------------------------------------------------
    # Comparison
    # ------------------------------------------------------

    if intent == "comparison":

        return [

            "Give me the key differences.",
            "Give an example of each.",
            "Which one is better and why?",
            "Give me an exam question on this."

        ]


    # ------------------------------------------------------
    # Advantages
    # ------------------------------------------------------

    if intent == "advantages":

        return [

            "What are the disadvantages?",
            "Give some examples.",
            "Why are they important?",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # Disadvantages
    # ------------------------------------------------------

    if intent == "disadvantages":

        return [

            "What are the advantages?",
            "Give some examples.",
            "How can these problems be reduced?",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # List
    # ------------------------------------------------------

    if intent == "list":

        return [

            "Explain each point.",
            "Give me examples.",
            "Which points are important for an exam?",
            "Give me a revision question."

        ]


    # ------------------------------------------------------
    # Process
    # ------------------------------------------------------

    if intent == "process":

        return [

            "Explain each step.",
            "Give me a simple example.",
            "Why is this process important?",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # Causes
    # ------------------------------------------------------

    if intent == "causes":

        return [

            "What are the effects?",
            "Explain the main cause.",
            "Give some examples.",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # Effects
    # ------------------------------------------------------

    if intent == "effects":

        return [

            "What are the causes?",
            "Explain the most important effect.",
            "Give some examples.",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # Examples
    # ------------------------------------------------------

    if intent == "examples":

        return [

            "Explain the examples.",
            "Give more examples.",
            "Where are they used?",
            "Give me an exam question."

        ]


    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    if intent == "summary":

        return [

            "Explain the topic in detail.",
            "Give me the key points.",
            "Give me an exam question.",
            "Test me on this topic."

        ]


    # ------------------------------------------------------
    # Examination
    # ------------------------------------------------------

    if intent == "exam":

        return [

            "Give me the model answer.",
            "Give me another question.",
            "Explain the answer.",
            "Test me without showing the answer."

        ]


    # ------------------------------------------------------
    # Calculation
    # ------------------------------------------------------

    if intent == "calculation":

        return [

            "Show the steps.",
            "Explain the formula.",
            "Give me another example.",
            "Give me a similar practice question."

        ]


    # ------------------------------------------------------
    # Education
    # ------------------------------------------------------

    if intent == "education":

        return [

            "Explain it simply.",
            "Give me an example.",
            "Give me the key points.",
            "Test me on this topic."

        ]


    # ------------------------------------------------------
    # Default
    # ------------------------------------------------------

    return [

        "Tell me more.",
        "Give an example.",
        "Give me the key points.",
        "Explain it simply."

    ]


# ==========================================================
# LEARNING TIP
# ==========================================================

def learning_tip(intent):

    tips = {

        "definition":
            "💡 Exam Tip: Learn the key definition first, then understand an example of the concept.",

        "explanation":
            "💡 Study Tip: Connect the concept to a real-life example to make it easier to remember.",

        "comparison":
            "💡 Exam Tip: When comparing two concepts, state clear differences point by point.",

        "advantages":
            "💡 Exam Tip: When asked for advantages, state each point clearly and briefly explain it.",

        "disadvantages":
            "💡 Exam Tip: When asked for disadvantages, identify each limitation and explain its effect.",

        "list":
            "💡 Exam Tip: Number your points clearly when a question asks you to list or state items.",

        "process":
            "💡 Study Tip: Learn the steps in the correct order and understand what happens at each stage.",

        "causes":
            "💡 Exam Tip: Separate the main causes clearly and explain how each one contributes to the problem.",

        "effects":
            "💡 Exam Tip: Distinguish between the cause of a problem and the effects it produces.",

        "examples":
            "💡 Study Tip: Examples help you connect theoretical knowledge to practical situations.",

        "summary":
            "💡 Study Tip: Focus on the key ideas rather than trying to memorize every sentence.",

        "exam":
            "💡 Exam Tip: Understand the concept first, then practise answering questions without looking at the answer.",

        "calculation":
            "💡 Exam Tip: Write the formula, substitute the values, show your working, and include the correct unit.",

        "translation":
            "💡 Language Tip: Practice using the translated word in a complete sentence.",

        "meaning":
            "💡 Study Tip: Understanding the meaning of a term makes it easier to remember and apply it."

    }


    return tips.get(

        intent,

        "💡 Study Tip: Keep asking questions and connect new concepts to examples you already understand."

    )


# ==========================================================
# CONFIDENCE ESTIMATION
# ==========================================================

def estimate_confidence(source):

    if not source:

        return "Low"


    source_lower = source.lower()


    # ------------------------------------------------------
    # Local educational knowledge
    # ------------------------------------------------------

    if "knowledge" in source_lower:

        return "Very High"


    # ------------------------------------------------------
    # Akan knowledge
    # ------------------------------------------------------

    if "akan" in source_lower:

        return "High"


    # ------------------------------------------------------
    # Educational web
    # ------------------------------------------------------

    if "educational_web" in source_lower:

        return "High"


    # ------------------------------------------------------
    # General web
    # ------------------------------------------------------

    if "web" in source_lower:

        return "Medium"


    return "Low"


# ==========================================================
# FORMAT ANSWER
# ==========================================================

def format_answer(
    answer,
    intent
):

    """
    Formats the answer according to the
    type of educational question.

    This keeps the response concise and
    examination-friendly.
    """

    if not answer:

        return ""


    answer = answer.strip()


    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if intent == "definition":

        return (

            "📖 Direct Answer\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Comparison
    # ------------------------------------------------------

    if intent == "comparison":

        return (

            "📖 Comparison\n\n"

            + answer

        )


    # ------------------------------------------------------
    # List
    # ------------------------------------------------------

    if intent == "list":

        return (

            "📋 Key Points\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Advantages
    # ------------------------------------------------------

    if intent == "advantages":

        return (

            "✅ Advantages\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Disadvantages
    # ------------------------------------------------------

    if intent == "disadvantages":

        return (

            "⚠️ Disadvantages\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Process
    # ------------------------------------------------------

    if intent == "process":

        return (

            "🔄 Process / Steps\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Causes
    # ------------------------------------------------------

    if intent == "causes":

        return (

            "🔎 Causes\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Effects
    # ------------------------------------------------------

    if intent == "effects":

        return (

            "📌 Effects\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Examples
    # ------------------------------------------------------

    if intent == "examples":

        return (

            "💡 Examples\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Calculation
    # ------------------------------------------------------

    if intent == "calculation":

        return (

            "🧮 Solution\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Examination
    # ------------------------------------------------------

    if intent == "exam":

        return (

            "📝 Examination Answer\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    if intent == "summary":

        return (

            "📚 Summary\n\n"

            + answer

        )


    # ------------------------------------------------------
    # Default
    # ------------------------------------------------------

    return (

        "📖 Answer\n\n"

        + answer

    )


# ==========================================================
# CREATE RESPONSE
# ==========================================================

def create_response(
    answer,
    source,
    intent,
    language
):

    """
    Creates the final response returned to the Flask
    application.

    The response is designed to be useful for students
    while still exposing source and intent information.
    """

    timestamp = datetime.now().strftime(

        "%d-%m-%Y %H:%M:%S"

    )


    confidence = estimate_confidence(
        source
    )


    followups = generate_follow_up(

        intent,

        language

    )


    tip = learning_tip(
        intent
    )


    formatted_answer = format_answer(

        answer,

        intent

    )


    # ======================================================
    # ASSISTANT NAME
    # ======================================================

    assistant = (

        "🇬🇭 Akan Educational Assistant"

        if language == "akan"

        else

        "🤖 Intelligent Educational Assistant"

    )


    # ======================================================
    # FINAL RESPONSE
    # ======================================================

    response = f"""
==================================================

{assistant}

--------------------------------------------------

{formatted_answer}

--------------------------------------------------

🎯 Question Type:
{intent.title()}

🌐 Language:
{language.title()}

📚 Source:
{source}

📊 Confidence:
{confidence}

--------------------------------------------------

{tip}

--------------------------------------------------

📌 Suggested Questions

1. {followups[0]}
2. {followups[1]}
3. {followups[2]}
4. {followups[3]}

🕒 {timestamp}

==================================================
"""


    return response.strip()