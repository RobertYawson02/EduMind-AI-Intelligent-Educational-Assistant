# ==========================================================
#
# ROUTER ENGINE
# Intelligent Multi-Engine Question Routing
#
# Stage 4
# Akan/Twi + Local Knowledge + Dynamic Web Retrieval
#
# ==========================================================

from model.akan_engine import (
    search_akan,
    format_akan_response,
    is_akan_related_question,
)

from model.knowledge_engine import (
    search_knowledge,
    format_knowledge,
)

from model.web_engine import (
    search_educational_web,
    search_akan_web,
    search_and_summarize,
)

from model.query_engine import (
    create_query_plan,
)
from model.ghana_qa_engine import search_ghana_qa


# ==========================================================
# ROUTE QUESTION
# ==========================================================

def route_question(
    question,
    topic=None,
    intent=None,
):
    """
    Routes a question through multiple knowledge engines.

    Processing order:

        1. Query Engine
        2. Akan / Twi Local Engine
        3. Local Knowledge Engine
        4. Dynamic Web Engine
        5. Web Fallback

    Returns a dictionary containing the results
    from the available engines.
    """

    print("\n======================================")
    print("🚦 ROUTER ENGINE")
    print("======================================")
    print("Question:", question)

    # ======================================================
    # VALIDATE QUESTION
    # ======================================================

    if not question or not str(question).strip():

        print("⚠️ Empty question.")

        return {
            "question": question,
            "topic": "",
            "intent": intent,
            "query_type": "general",
            "language": "unknown",
            "is_akan": False,
            "target": "",
            "akan": None,
            "knowledge": None,
            "web": None,
            "sources": [],
        }

    question = str(question).strip()

    # ======================================================
    # INITIAL RESULTS
    # ======================================================

    results = {
        "question": question,
        "topic": topic or "",
        "intent": intent,
        "query_type": "general",
        "language": "unknown",
        "is_akan": False,
        "target": "",
        "akan": None,
        "ghana_qa": None,
        "knowledge": None,
        "web": None,
        "sources": [],
    }

    # ======================================================
    # QUERY ENGINE
    # ======================================================

    expanded_queries = []

    try:

        print("\n🧠 Running Query Planner...")

        query_plan = create_query_plan(
            question
        )

        expanded_queries = query_plan.get(
            "queries",
            []
        )

        detected_topic = query_plan.get(
            "topic",
            ""
        )

        query_type = query_plan.get(
            "query_type",
            "general"
        )

        language = query_plan.get(
            "language",
            "unknown"
        )

        is_akan = query_plan.get(
            "is_akan",
            False
        )

        target = query_plan.get(
            "target",
            ""
        )

        results["query_type"] = query_type
        results["language"] = language
        results["is_akan"] = is_akan
        results["target"] = target

        if not topic:
            topic = detected_topic

        if not topic:
            topic = target

        results["topic"] = topic or ""

        print("🧠 Query Type:", query_type)
        print("🌐 Language:", language)
        print("🇬🇭 Akan Detected:", is_akan)
        print("🎯 Target:", target)
        print("🔎 Search Topic:", topic)
        print(
            "🔎 Expanded Queries:",
            len(expanded_queries)
        )

        for index, query in enumerate(
            expanded_queries,
            start=1
        ):
            print(
                f"   {index}. {query}"
            )

    except Exception as e:

        print(
            "⚠️ Query Engine Error:",
            e
        )

        expanded_queries = [
            question
        ]

        results["topic"] = (
            topic
            or question
        )

    # ======================================================
    # GHANA-QA DATASET ENGINE (OPTIONAL)
    # ======================================================

    try:

        print("\n🇬🇭 Checking Ghana-QA dataset...")
        language_hint = "akan" if results["is_akan"] else None
        ghana_candidates = search_ghana_qa(
            question,
            language=language_hint,
            limit=5,
        )

        if ghana_candidates:
            dataset_name = str(ghana_candidates[0].get("dataset", "")) if ghana_candidates else ""
            source_key = "ghana_qa_sample" if dataset_name == "ghana_qa_sample.csv" else "ghana_qa"
            results[source_key] = ghana_candidates
            results["sources"].append("Curated Ghanaian QA Sample" if source_key == "ghana_qa_sample" else "Ghana-QA Dataset")
            print("🇬🇭 Ghana-QA candidates:", len(ghana_candidates))
        else:
            results["ghana_qa"] = None

    except Exception as e:
        print("⚠️ Ghana-QA Engine Error:", e)
        results["ghana_qa"] = None

    # ======================================================
    # AKAN / TWI LOCAL ENGINE
    # ======================================================

    akan_result = None
    akan_mode = None

    try:

        print(
            "\n🇬🇭 Checking Akan / Twi Local Engine..."
        )

        # The lexical dictionary contains short words that can occur inside
        # unrelated English text.  Consult it only for an Akan query or an
        # explicit translation request, rather than treating every question as
        # a possible dictionary lookup.
        if (
            results["is_akan"]
            or intent == "translation"
            or is_akan_related_question(question)
        ):
            akan_result, akan_mode = search_akan(question)

        if akan_result:

            print(
                "🇬🇭 Routed → Akan Local Engine"
            )

            print(
                "🇬🇭 Akan Mode:",
                akan_mode
            )

            results["akan"] = format_akan_response(
                akan_result,
                akan_mode,
                question
            )

            results["sources"].append(
                "Akan / Twi Lexical Knowledge Base"
            )

        else:

            print(
                "No Akan lexical lookup required or no lexical match."
            )

    except Exception as e:

        print(
            "⚠️ Akan Engine Error:",
            e
        )

    # ======================================================
    # LOCAL KNOWLEDGE ENGINE
    # ======================================================

    try:

        print(
            "\n📚 Checking Local Knowledge Engine..."
        )

        # Preserve the full wording so retrieval can distinguish a definition
        # request from related variants such as steps or applications.
        knowledge_topic = question

        knowledge = search_knowledge(
            knowledge_topic
        )

        if knowledge:

            print(
                "📚 Routed → Knowledge Engine"
            )

            results["knowledge"] = {
                "answer": format_knowledge(knowledge),
                "retrieval_score": knowledge.get("retrieval_score", 0.0),
                "topic": knowledge.get("topic", ""),
                "category": knowledge.get("category", ""),
            }

            results["sources"].append(
                "Local Educational Knowledge Base"
            )

        else:

            print(
                "📚 No local knowledge match."
            )

    except Exception as e:

        print(
            "⚠️ Knowledge Engine Error:",
            e
        )

    # ======================================================
    # DYNAMIC WEB RETRIEVAL
    # ======================================================

    try:

        print(
            "\n🌍 Checking Dynamic Web Retrieval..."
        )

        # Local educational and lexical records are the preferred evidence.
        # Do not make an unnecessary live network request when either has
        # already answered the question; this also keeps local demonstrations
        # responsive when internet access is unavailable.
        # Use local evidence as the primary source, but supplement it with
        # web evidence for intents where breadth, recency, comparison, or
        # explanation materially improves the answer. This keeps the system
        # useful offline while still exercising the open-web retrieval path.
        web_supplement_intents = {
            "applications", "comparison", "explanation", "summary",
            "process", "causes", "effects", "exam", "education",
            "general", "list", "examples",
        }
        needs_web_supplement = (
            intent in web_supplement_intents
            or not results["knowledge"] and not results["akan"]
        )

        if results["is_akan"] and not results["knowledge"]:
            print("Akan question without strong local educational evidence; using Akan web retrieval.")

        if results["is_akan"] and not results["knowledge"]:

            # ------------------------------------------------
            # AKAN / TWI WEB RETRIEVAL
            # ------------------------------------------------

            print(
                "🇬🇭 Routing → Akan/Twi Web Retrieval"
            )

            akan_target = (
                results.get("target")
                or results.get("topic")
                or question
            )

            web_results = search_akan_web(
                akan_target,
                query_type=results["query_type"],
                limit=5,
            )

            if web_results:

                results["web"] = web_results

                results["sources"].append(
                    "Dynamic Akan/Twi Web Sources"
                )

                print(
                    "🇬🇭 Akan Web Results:",
                    len(web_results)
                )

            else:

                print(
                    "⚠️ No Akan/Twi web results found."
                )

        elif needs_web_supplement:

            # ------------------------------------------------
            # GENERAL EDUCATIONAL WEB RETRIEVAL
            # ------------------------------------------------

            print(
                "📚 Routing → Educational Web Retrieval"
            )

            if not expanded_queries:

                expanded_queries = [
                    question
                ]

            web_results = search_educational_web(
                expanded_queries
            )

            if web_results:

                results["web"] = web_results

                results["sources"].append(
                    "Dynamic Educational Web Sources"
                )

                print(
                    "🌍 Web Results:",
                    len(web_results)
                )

            else:

                print(
                    "⚠️ No educational web results found."
                )

    except Exception as e:

        print(
            "⚠️ Web Engine Error:",
            e
        )

    # ======================================================
    # WEB FALLBACK
    # ======================================================

    if (
        results["web"] is None
        and not results["akan"]
        and not results["knowledge"]
    ):

        try:

            print(
                "\n🌍 Attempting Web Fallback..."
            )

            if results["is_akan"]:

                # ------------------------------------------------
                # AKAN / TWI FALLBACK
                # ------------------------------------------------

                fallback_target = (
                    results.get("target")
                    or results.get("topic")
                    or question
                )

                fallback_results = search_akan_web(
                    fallback_target,
                    query_type=results["query_type"],
                    limit=5,
                )

                if fallback_results:

                    results["web"] = fallback_results

                    results["sources"].append(
                        "Akan/Twi Web Fallback"
                    )

                    print(
                        "🇬🇭 Akan/Twi fallback returned results."
                    )

                else:

                    print(
                        "⚠️ Akan/Twi fallback returned nothing."
                    )

            else:

                # ------------------------------------------------
                # GENERAL WEB FALLBACK
                # ------------------------------------------------

                fallback_queries = []

                if expanded_queries:

                    fallback_queries.extend(
                        expanded_queries[:3]
                    )

                if question not in fallback_queries:

                    fallback_queries.append(
                        question
                    )

                fallback = search_and_summarize(
                    fallback_queries
                )

                if fallback:

                    results["web"] = fallback

                    results["sources"].append(
                        "Web Fallback"
                    )

                    print(
                        "🌍 Web fallback returned results."
                    )

                else:

                    print(
                        "⚠️ Web fallback returned nothing."
                    )

        except Exception as e:

            print(
                "⚠️ Web Fallback Error:",
                e
            )

    # ======================================================
    # REMOVE DUPLICATE SOURCES
    # ======================================================

    results["sources"] = list(
        dict.fromkeys(
            results["sources"]
        )
    )

    # ======================================================
    # ROUTING SUMMARY
    # ======================================================

    print(
        "\n--------------------------------------"
    )

    print(
        "ROUTING SUMMARY"
    )

    print(
        "Akan:",
        "Available"
        if results["akan"]
        else "None"
    )

    print(
        "Knowledge:",
        "Available"
        if results["knowledge"]
        else "None"
    )

    print(
        "Web:",
        "Available"
        if results["web"]
        else "None"
    )

    print(
        "Language:",
        results["language"]
    )

    print(
        "Query Type:",
        results["query_type"]
    )

    print(
        "Sources:",
        len(results["sources"])
    )

    print(
        "--------------------------------------"
    )

    return results


# ==========================================================
# GET PRIMARY ANSWER
# ==========================================================

def get_primary_answer(results):
    """
    Select the strongest available answer.

    Priority:

        1. Akan answer
        2. Local knowledge
        3. Web answer
    """

    if not results:
        return None

    if results.get("akan"):
        return results["akan"]

    if results.get("knowledge"):
        return results["knowledge"]

    if results.get("web"):
        return results["web"]

    return None


# ==========================================================
# GET ALL AVAILABLE ANSWERS
# ==========================================================

def get_available_answers(results):
    """
    Return all available engine answers.
    """

    if not results:
        return []

    answers = []

    if results.get("akan"):

        answers.append({
            "source": "akan",
            "answer": results["akan"],
        })

    if results.get("knowledge"):

        answers.append({
            "source": "knowledge",
            "answer": results["knowledge"],
        })

    if results.get("web"):

        answers.append({
            "source": "web",
            "answer": results["web"],
        })

    return answers


# ==========================================================
# FORMAT ROUTER RESPONSE
# ==========================================================

def format_router_response(results):
    """
    Produce a unified response from all available engines.

    This function is useful for the Flask/API layer.
    """

    if not results:
        return None

    sections = []

    # ======================================================
    # AKAN
    # ======================================================

    if results.get("akan"):

        sections.append(
            results["akan"]
        )

    # ======================================================
    # LOCAL KNOWLEDGE
    # ======================================================

    if results.get("knowledge"):

        sections.append(
            "📚 Local Educational Knowledge\n\n"
            + str(
                results["knowledge"]
            )
        )

    # ======================================================
    # WEB
    # ======================================================

    web = results.get(
        "web"
    )

    if web:

        if isinstance(
            web,
            list
        ):

            web_section = [
                "🌍 Dynamic Web Knowledge"
            ]

            for index, item in enumerate(
                web[:5],
                start=1
            ):

                if not isinstance(
                    item,
                    dict
                ):
                    continue

                title = item.get(
                    "title",
                    "Web Source"
                )

                summary = item.get(
                    "summary",
                    ""
                )

                domain = item.get(
                    "domain",
                    ""
                )

                web_section.append(
                    f"\n{index}. {title}"
                )

                if summary:

                    web_section.append(
                        f"\n{summary}"
                    )

                if domain:

                    web_section.append(
                        f"\nSource: {domain}"
                    )

            if len(web_section) > 1:

                sections.append(
                    "\n".join(
                        web_section
                    )
                )

        else:

            sections.append(
                str(web)
            )

    # ======================================================
    # NO ANSWER
    # ======================================================

    if not sections:

        return (
            "I could not find a reliable answer "
            "from the available knowledge sources."
        )

    # ======================================================
    # FINAL RESPONSE
    # ======================================================

    return "\n\n".join(
        sections
    )


# ==========================================================
# ROUTER STATISTICS
# ==========================================================

def router_statistics(results):
    """
    Return useful statistics about the routing operation.
    """

    if not results:

        return {
            "akan": False,
            "knowledge": False,
            "web": False,
            "source_count": 0,
        }

    return {
        "akan": bool(
            results.get("akan")
        ),

        "knowledge": bool(
            results.get("knowledge")
        ),

        "web": bool(
            results.get("web")
        ),

        "source_count": len(
            results.get(
                "sources",
                []
            )
        ),

        "sources": results.get(
            "sources",
            []
        ),

        "query_type": results.get(
            "query_type",
            "general"
        ),

        "language": results.get(
            "language",
            "unknown"
        ),

        "is_akan": results.get(
            "is_akan",
            False
        ),

        "target": results.get(
            "target",
            ""
        ),

        "topic": results.get(
            "topic",
            ""
        ),
    }


# ==========================================================
# SIMPLE ROUTER TEST
# ==========================================================

def test_router():

    test_questions = [

        "What is artificial intelligence?",

        "Explain machine learning",

        "What is the meaning of nsuo?",

        "What does nsuo mean in Twi?",

        "What is the meaning of ɔdɔ?",

        "Translate water into Twi",

        "Give me an example of nsuo",

        "What are synonyms of ɔdɔ?",

        "What is the opposite of ɔdɔ?",

        "What does nsuo retɔ mean?",

        "How do you say I am hungry in Twi?",

    ]

    for question in test_questions:

        print(
            "\n\n######################################"
        )

        print(
            "QUESTION:",
            question
        )

        print(
            "######################################"
        )

        results = route_question(
            question
        )

        print(
            "\nROUTER STATISTICS:"
        )

        stats = router_statistics(
            results
        )

        for key, value in stats.items():

            print(
                f"{key}: {value}"
            )

        print(
            "\n======================================"
        )

        print(
            "FINAL ROUTER RESPONSE"
        )

        print(
            "======================================"
        )

        final_response = format_router_response(
            results
        )

        print(
            final_response
        )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_router()


# ==========================================================
# END OF ROUTER ENGINE
# ==========================================================
