# ==========================================================
#
# CONVERSATION ENGINE
# Responsible for storing and resolving conversation context
#
# ==========================================================

import os
import json
import re
from datetime import datetime


# ==========================================================
# CONVERSATION STORAGE LOCATION
# ==========================================================

def get_storage_path():
    """
    Returns the path to the conversation history file.
    """

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    data_dir = os.path.join(
        base_dir,
        "data"
    )

    conversation_file = os.path.join(
        data_dir,
        "conversation_history.json"
    )

    return conversation_file


# ==========================================================
# CREATE STORAGE FILE IF NOT AVAILABLE
# ==========================================================

def initialize_storage():
    """
    Creates the data directory and conversation file
    if they do not already exist.
    """

    file_path = get_storage_path()

    data_dir = os.path.dirname(
        file_path
    )

    # ------------------------------------------------------
    # Create data directory if it does not exist.
    # ------------------------------------------------------

    os.makedirs(
        data_dir,
        exist_ok=True
    )

    # ------------------------------------------------------
    # Create conversation file if it does not exist.
    # ------------------------------------------------------

    if not os.path.exists(file_path):

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print(
                "💾 Conversation storage initialized."
            )

        except OSError as e:

            print(
                "⚠️ Could not create conversation storage:"
            )

            print(e)


# ==========================================================
# LOAD CONVERSATION HISTORY
# ==========================================================

def load_conversation():
    """
    Safely loads conversation history.

    Returns:
        list: Conversation history.
    """

    initialize_storage()

    file_path = get_storage_path()

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        # --------------------------------------------------
        # Make sure the JSON contains a list.
        # --------------------------------------------------

        if not isinstance(
            data,
            list
        ):

            print(
                "⚠️ Conversation history must contain a JSON list."
            )

            return []

        return data

    except FileNotFoundError:

        # --------------------------------------------------
        # Safety fallback if the file disappears.
        # --------------------------------------------------

        initialize_storage()

        return []

    except json.JSONDecodeError as e:

        print(
            "⚠️ Invalid conversation history JSON:"
        )

        print(e)

        return []

    except OSError as e:

        print(
            "⚠️ Could not read conversation history:"
        )

        print(e)

        return []

    except Exception as e:

        print(
            "⚠️ Conversation loading error:"
        )

        print(e)

        return []


# ==========================================================
# SAVE USER INTERACTION
# ==========================================================

def save_conversation(
    question,
    topic,
    intent,
    language
):
    """
    Saves one user interaction while preserving
    the existing JSON structure.
    """

    # ------------------------------------------------------
    # Handle empty questions safely.
    # ------------------------------------------------------

    if question is None:

        question = ""

    question = str(
        question
    ).strip()

    # ------------------------------------------------------
    # Handle missing topic safely.
    # ------------------------------------------------------

    if topic is None:

        topic = ""

    topic = str(
        topic
    ).strip()

    # ------------------------------------------------------
    # Handle missing intent safely.
    # ------------------------------------------------------

    if intent is None:

        intent = "general"

    intent = str(
        intent
    ).strip()

    # ------------------------------------------------------
    # Handle missing language safely.
    # ------------------------------------------------------

    if language is None:

        language = "english"

    language = str(
        language
    ).strip()

    # ------------------------------------------------------
    # Load existing conversation history.
    # ------------------------------------------------------

    history = load_conversation()

    conversation = {

        "question": question,

        "topic": topic,

        "intent": intent,

        "language": language,

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    }

    history.append(
        conversation
    )

    file_path = get_storage_path()

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError as e:

        print(
            "⚠️ Could not save conversation:"
        )

        print(e)

        return False


# ==========================================================
# GET LAST DISCUSSION TOPIC
# ==========================================================

def get_previous_topic():
    """
    Returns the topic from the most recent
    valid conversation entry.
    """

    history = load_conversation()

    if not history:

        return None

    # ------------------------------------------------------
    # Search backward for the most recent valid topic.
    # ------------------------------------------------------

    for entry in reversed(history):

        if not isinstance(
            entry,
            dict
        ):

            continue

        topic = entry.get(
            "topic"
        )

        if topic is None:

            continue

        topic = str(
            topic
        ).strip()

        if topic:

            return topic

    return None


# ==========================================================
# CHECK WHETHER QUESTION HAS A CLEAR TOPIC
# ==========================================================

def has_explicit_topic(question):
    """
    Determines whether the question contains a clear
    subject/topic of its own.

    This prevents the conversation engine from replacing
    a clearly stated topic with the previous topic.

    Example:

        What are the applications of artificial intelligence?

    contains the explicit topic:

        artificial intelligence

    Therefore the previous topic should NOT replace it.
    """

    if question is None:

        return False

    question = str(
        question
    ).strip()

    if not question:

        return False

    q = question.lower()

    # A leading pronoun references earlier context rather than introducing a
    # new topic (for example, "What are its applications?").
    if re.search(
        r"^(?:what\s+(?:is|are)|how|why|when|where)\s+"
        r"(?:it|its|this|that|these|those)\b",
        q,
    ):
        return False

    # ------------------------------------------------------
    # Common question structures that normally contain
    # an explicit subject.
    # ------------------------------------------------------

    explicit_topic_patterns = [

        r"\bwhat\s+is\s+.+",

        r"\bwhat\s+are\s+.+",

        r"\bwhat\s+was\s+.+",

        r"\bwhat\s+were\s+.+",

        r"\bdefine\s+.+",

        r"\bdefinition\s+of\s+.+",

        r"\bmeaning\s+of\s+.+",

        r"\bwhat\s+does\s+.+\s+mean",

        r"\bexplain\s+.+",

        r"\bdescribe\s+.+",

        r"\btell\s+me\s+about\s+.+",

        r"\bdiscuss\s+.+",

        r"\bcompare\s+.+",

        r"\bdifference\s+between\s+.+",

        r"\bdifferences\s+between\s+.+",

        r"\badvantages\s+of\s+.+",

        r"\bdisadvantages\s+of\s+.+",

        r"\bapplications\s+of\s+.+",

        r"\buses\s+of\s+.+",

        r"\bexamples\s+of\s+.+",

        r"\bcauses\s+of\s+.+",

        r"\beffects\s+of\s+.+",

        r"\btypes\s+of\s+.+",

        r"\bcharacteristics\s+of\s+.+",

        r"\bfeatures\s+of\s+.+",

        r"\bcomponents\s+of\s+.+",

        r"\bfunctions\s+of\s+.+",

        r"\bimportance\s+of\s+.+",

        r"\bhow\s+does\s+.+",

        r"\bhow\s+do\s+.+",

        r"\bhow\s+can\s+.+",

        r"\bwhere\s+is\s+.+\s+used",

        r"\bwhere\s+are\s+.+\s+used",

        r"\bhow\s+is\s+.+\s+used",

        r"\bhow\s+are\s+.+\s+used",

        r"\bcalculate\s+.+",

        r"\bsolve\s+.+",

        r"\btranslate\s+.+",

    ]

    # ------------------------------------------------------
    # Check whether any explicit-topic pattern matches.
    # ------------------------------------------------------

    for pattern in explicit_topic_patterns:

        if re.search(
            pattern,
            q
        ):

            return True

    return False


# ==========================================================
# DETERMINE WHETHER QUESTION IS A FOLLOW-UP
# ==========================================================

def is_follow_up_question(question):
    """
    Determines whether the current question is likely
    dependent on previous conversation context.
    """

    if question is None:

        return False

    question = str(
        question
    ).strip()

    if not question:

        return False

    q = question.lower()

    # ------------------------------------------------------
    # If the question clearly contains its own topic,
    # it should NOT inherit the previous topic.
    # ------------------------------------------------------

    if has_explicit_topic(q):

        return False

    # ------------------------------------------------------
    # Direct reference words.
    # ------------------------------------------------------

    follow_up_words = [

        "it",

        "its",

        "they",

        "them",

        "this",

        "that",

        "those",

        "these"

    ]

    for word in follow_up_words:

        pattern = (
            r"\b"
            + re.escape(word)
            + r"\b"
        )

        if re.search(
            pattern,
            q
        ):

            return True

    # ------------------------------------------------------
    # Context-dependent educational questions.
    #
    # These can be understood from the previous topic.
    # ------------------------------------------------------

    follow_up_patterns = [

        r"^applications$",

        r"^advantages$",

        r"^disadvantages$",

        r"^examples$",

        r"^uses$",

        r"^importance$",

        r"^limitations$",

        r"^benefits$",

        r"^drawbacks$",

        r"^types$",

        r"^characteristics$",

        r"^features$",

        r"^components$",

        r"^functions$",

        r"^causes$",

        r"^effects$",

        r"^more$",

        r"^tell me more$",

        r"^explain more$",

        r"^explain further$",

        r"^give more examples$",

        r"^give me more examples$",

        r"^what about it$",

        r"^what about this$",

        r"^what about that$",

        r"^why$",

        r"^how$",

        r"^where$",

        r"^when$",

        r"^who$",

        r"^and why$",

        r"^and how$",

        r"^what else$",

    ]

    for pattern in follow_up_patterns:

        if re.search(
            pattern,
            q
        ):

            return True

    return False


# ==========================================================
# RESOLVE FOLLOW-UP QUESTIONS
# ==========================================================

def resolve_topic(question):
    """
    Determines whether the current question
    depends on previous conversation.

    The previous topic is returned only when the
    question appears to be a genuine follow-up.

    Examples:

        Previous topic:
            artificial intelligence

        "What are its applications?"
            -> artificial intelligence

        "What are the advantages?"
            -> artificial intelligence

        "Give me examples."
            -> artificial intelligence

        "What are the applications of artificial intelligence?"
            -> None

        "What is Python?"
            -> None
    """

    # ------------------------------------------------------
    # Handle empty questions safely.
    # ------------------------------------------------------

    if question is None:

        return None

    question = str(
        question
    ).strip()

    if not question:

        return None

    # ------------------------------------------------------
    # Check whether this is actually a follow-up.
    # ------------------------------------------------------

    if not is_follow_up_question(
        question
    ):

        return None

    # ------------------------------------------------------
    # Retrieve previous topic.
    # ------------------------------------------------------

    previous_topic = get_previous_topic()

    if not previous_topic:

        return None

    return previous_topic


# ==========================================================
# CLEAR MEMORY
# ==========================================================

def clear_conversation():
    """
    Clears all stored conversation history.
    """

    file_path = get_storage_path()

    # ------------------------------------------------------
    # Make sure storage exists first.
    # ------------------------------------------------------

    initialize_storage()

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            "[CLEARED] Conversation history cleared."
        )

        return True

    except OSError as e:

        print(
            "⚠️ Could not clear conversation history:"
        )

        print(e)

        return False


# ==========================================================
# TEST CONVERSATION ENGINE
# ==========================================================

def test_conversation_engine():
    """
    Tests:

        1. Storage initialization
        2. Empty question handling
        3. Conversation saving
        4. Conversation loading
        5. Previous topic retrieval
        6. Genuine follow-up detection
        7. Explicit-topic protection
        8. Whole-word matching
        9. JSON structure
        10. Storage path
    """

    print(
        "\n=========================================="
    )

    print(
        "💬 CONVERSATION ENGINE TEST"
    )

    print(
        "=========================================="
    )

    # ------------------------------------------------------
    # 1. Initialize storage
    # ------------------------------------------------------

    print(
        "\n1. Testing storage initialization..."
    )

    initialize_storage()

    storage_path = get_storage_path()

    print(
        "Storage Path:",
        storage_path
    )

    print(
        "File Exists:",
        os.path.exists(storage_path)
    )

    # ------------------------------------------------------
    # 2. Clear previous test memory
    # ------------------------------------------------------

    print(
        "\n2. Clearing old test memory..."
    )

    clear_conversation()

    # ------------------------------------------------------
    # 3. Test empty question
    # ------------------------------------------------------

    print(
        "\n3. Testing empty question..."
    )

    empty_result = resolve_topic("")

    print(
        "Empty Question Result:",
        empty_result
    )

    # ------------------------------------------------------
    # 4. Save first conversation
    # ------------------------------------------------------

    print(
        "\n4. Saving first conversation..."
    )

    saved = save_conversation(
        question="What is artificial intelligence?",
        topic="artificial intelligence",
        intent="definition",
        language="english"
    )

    print(
        "Conversation Saved:",
        saved
    )

    # ------------------------------------------------------
    # 5. Test previous topic
    # ------------------------------------------------------

    print(
        "\n5. Testing previous topic..."
    )

    previous_topic = get_previous_topic()

    print(
        "Previous Topic:",
        previous_topic
    )

    # ------------------------------------------------------
    # 6. Genuine follow-up tests
    # ------------------------------------------------------

    print(
        "\n6. Testing genuine follow-up questions..."
    )

    follow_up_questions = [

        "What are its applications?",

        "What are the advantages?",

        "Give me examples.",

        "Explain this.",

        "Tell me more.",

        "What about it?"

    ]

    for question in follow_up_questions:

        result = resolve_topic(
            question
        )

        print(
            f"\nQuestion: {question}"
        )

        print(
            f"Resolved Topic: {result}"
        )

    # ------------------------------------------------------
    # 7. Test explicit topics
    # ------------------------------------------------------

    print(
        "\n7. Testing explicit-topic protection..."
    )

    explicit_topic_questions = [

        "What are the applications of artificial intelligence?",

        "What is Python?",

        "What are the advantages of social media?",

        "Explain machine learning.",

        "Where is artificial intelligence used?",

        "What are examples of databases?"

    ]

    for question in explicit_topic_questions:

        result = resolve_topic(
            question
        )

        print(
            f"\nQuestion: {question}"
        )

        print(
            f"Resolved Topic: {result}"
        )

    # ------------------------------------------------------
    # 8. Whole-word matching test
    # ------------------------------------------------------

    print(
        "\n8. Testing whole-word matching..."
    )

    whole_word_questions = [

        "Tell me about item.",

        "Tell me about with.",

        "Tell me about this.",

        "Explain that.",

        "What are its uses?"

    ]

    for question in whole_word_questions:

        result = resolve_topic(
            question
        )

        print(
            f"\nQuestion: {question}"
        )

        print(
            f"Resolved Topic: {result}"
        )

    # ------------------------------------------------------
    # 9. Load conversation history
    # ------------------------------------------------------

    print(
        "\n9. Testing conversation loading..."
    )

    history = load_conversation()

    print(
        "Stored Conversations:",
        len(history)
    )

    print(
        json.dumps(
            history,
            indent=4,
            ensure_ascii=False
        )
    )

    # ------------------------------------------------------
    # 10. Test JSON structure
    # ------------------------------------------------------

    print(
        "\n10. Checking JSON structure..."
    )

    if history:

        required_fields = [

            "question",

            "topic",

            "intent",

            "language",

            "timestamp"

        ]

        last_entry = history[-1]

        for field in required_fields:

            print(
                f"{field}:",
                field in last_entry
            )

    # ------------------------------------------------------
    # Final result
    # ------------------------------------------------------

    print(
        "\n=========================================="
    )

    print(
        "✅ CONVERSATION ENGINE TEST COMPLETE"
    )

    print(
        "=========================================="
    )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_conversation_engine()


# ==========================================================
# END OF CONVERSATION ENGINE
# ==========================================================
