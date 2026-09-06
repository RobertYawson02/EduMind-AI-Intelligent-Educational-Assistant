# ==========================================================
#
# WEB ENGINE
# Intelligent Multi-Source Educational + Akan/Twi Retrieval
#
# Stage 3
#
# Responsibilities:
# 1. General educational web retrieval
# 2. Akan/Twi web retrieval
# 3. Source quality ranking
# 4. Query relevance ranking
# 5. Duplicate removal
# 6. Multi-source retrieval
# 7. Dictionary/source specialization
# 8. Intent-aware Akan/Twi searching
# 9. Structured web evidence
#
# ==========================================================

from ddgs import DDGS
from urllib.parse import urlparse
import re


# ==========================================================
# TRUSTED EDUCATIONAL DOMAINS
# ==========================================================

EDUCATIONAL_DOMAINS = {
    "openstax.org",
    "ocw.mit.edu",
    "mit.edu",
    "stanford.edu",
    "harvard.edu",
    "berkeley.edu",
    "ox.ac.uk",
    "cam.ac.uk",
    "khanacademy.org",
    "britannica.com",
    "wikipedia.org",
}


# ==========================================================
# AKAN / TWI DICTIONARY DOMAINS
# ==========================================================

AKAN_DICTIONARY_DOMAINS = {
    "akandictionary.com",
    "glosbe.com",
    "afiaghana.com",
    "learnakan.com",
}


# ==========================================================
# AKAN / TWI NLP / RESEARCH DOMAINS
# ==========================================================

AKAN_NLP_DOMAINS = {
    "ghananlp.org",
    "huggingface.co",
}


# ==========================================================
# EDUCATIONAL KEYWORDS
# ==========================================================

EDUCATIONAL_KEYWORDS = [
    "definition",
    "defined",
    "education",
    "learning",
    "study",
    "course",
    "textbook",
    "lesson",
    "chapter",
    "concept",
    "principle",
    "theory",
    "example",
    "examples",
    "advantages",
    "disadvantages",
    "benefits",
    "limitations",
    "characteristics",
    "types",
    "classification",
    "process",
    "procedure",
    "explanation",
    "academic",
    "students",
    "university",
    "college",
    "school",
    "research",
    "lecture",
    "notes",
    "computer",
    "science",
    "technology",
]


# ==========================================================
# AKAN / TWI KEYWORDS
# ==========================================================

AKAN_KEYWORDS = [
    "twi",
    "akan",
    "english",
    "translation",
    "dictionary",
    "meaning",
    "word",
    "phrase",
    "sentence",
    "vocabulary",
    "grammar",
    "usage",
    "example",
    "synonym",
    "antonym",
    "dialect",
    "asante",
    "akuapem",
]


# ==========================================================
# GET DOMAIN
# ==========================================================

def get_domain(url):
    """
    Extract the main domain from a URL.
    """

    if not url:
        return ""

    try:

        parsed = urlparse(
            str(url)
        )

        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        return domain.strip()

    except Exception:

        return ""


# ==========================================================
# DOMAIN CATEGORY
# ==========================================================

def get_domain_category(domain):
    """
    Determine the category of a web source.
    """

    if not domain:
        return "unknown"

    if domain in AKAN_DICTIONARY_DOMAINS:
        return "akan_dictionary"

    if domain in AKAN_NLP_DOMAINS:
        return "akan_nlp"

    if domain.endswith(".edu"):
        return "academic"

    if domain in EDUCATIONAL_DOMAINS:

        if domain in {
            "wikipedia.org",
            "britannica.com",
        }:
            return "reference"

        return "educational"

    if domain.endswith("openstax.org"):
        return "educational"

    if domain.endswith("khanacademy.org"):
        return "educational"

    return "general"


# ==========================================================
# SOURCE QUALITY SCORE
# ==========================================================

def get_source_score(result, akan=False):
    """
    Assign a source-quality score.

    Akan dictionary sources receive the strongest
    priority for Akan/Twi lexical questions.
    """

    url = result.get(
        "href",
        "",
    )

    domain = get_domain(
        url
    )

    score = 0

    # ------------------------------------------------------
    # Akan dictionary sources
    # ------------------------------------------------------

    if domain == "akandictionary.com":
        score += 35

    elif domain == "glosbe.com":
        score += 32

    elif domain == "afiaghana.com":
        score += 30

    elif domain == "learnakan.com":
        score += 28

    # ------------------------------------------------------
    # Akan NLP / research
    # ------------------------------------------------------

    elif domain == "ghananlp.org":
        score += 24

    elif domain == "huggingface.co":
        score += 16

    # ------------------------------------------------------
    # Academic domains
    # ------------------------------------------------------

    if domain.endswith(".edu"):
        score += 12

    # ------------------------------------------------------
    # Open educational resources
    # ------------------------------------------------------

    if domain.endswith("openstax.org"):
        score += 15

    if domain.endswith("ocw.mit.edu"):
        score += 15

    # ------------------------------------------------------
    # Educational platforms
    # ------------------------------------------------------

    if domain.endswith("khanacademy.org"):
        score += 12

    # ------------------------------------------------------
    # Known universities
    # ------------------------------------------------------

    if domain in {
        "mit.edu",
        "stanford.edu",
        "harvard.edu",
        "berkeley.edu",
        "ox.ac.uk",
        "cam.ac.uk",
    }:
        score += 12

    # ------------------------------------------------------
    # Reference sources
    # ------------------------------------------------------

    if domain.endswith("britannica.com"):
        score += 8

    if domain.endswith("wikipedia.org"):
        score += 3

    # ------------------------------------------------------
    # Penalize irrelevant general sources for Akan searches
    # ------------------------------------------------------

    if akan:

        if domain not in AKAN_DICTIONARY_DOMAINS \
                and domain not in AKAN_NLP_DOMAINS:

            score -= 3

    # ------------------------------------------------------
    # Minimum score
    # ------------------------------------------------------

    if score < 1:
        score = 1

    return score


# ==========================================================
# TEXT TOKENIZATION
# ==========================================================

def tokenize(text):
    """
    Convert text into searchable words.

    Supports Akan characters such as:
        ɔ
        ɛ
        ŋ
    """

    if not text:
        return []

    text = str(
        text
    ).lower()

    words = re.findall(
        r"[a-zA-ZÀ-ÖØ-öø-ÿɔɛŋ]+",
        text,
    )

    return words


# ==========================================================
# QUERY RELEVANCE
# ==========================================================

def calculate_query_relevance(
    result,
    query,
):
    """
    Measure how closely the result matches
    the search query.
    """

    title = result.get(
        "title",
        "",
    ).lower()

    body = result.get(
        "body",
        "",
    ).lower()

    query_words = tokenize(
        query
    )

    if not query_words:
        return 0

    score = 0

    for word in query_words:

        if len(word) < 2:
            continue

        # Title match
        if word in title:
            score += 8

        # Body match
        if word in body:
            score += 3

    return score


# ==========================================================
# AKAN RELEVANCE
# ==========================================================

def calculate_akan_relevance(
    result,
    query,
):
    """
    Calculate Akan/Twi-specific relevance.

    Exact target matches receive strong priority.
    """

    title = result.get(
        "title",
        "",
    ).lower()

    body = result.get(
        "body",
        "",
    ).lower()

    text = (
        title
        + " "
        + body
    )

    query_lower = str(
        query
    ).lower().strip()

    score = 0

    # ------------------------------------------------------
    # Exact phrase
    # ------------------------------------------------------

    if query_lower:

        if query_lower in title:
            score += 25

        elif query_lower in body:
            score += 18

    # ------------------------------------------------------
    # Individual target words
    # ------------------------------------------------------

    query_words = tokenize(
        query_lower
    )

    for word in query_words:

        if len(word) < 2:
            continue

        if word in title:
            score += 10

        elif word in body:
            score += 5

    # ------------------------------------------------------
    # Akan/Twi indicators
    # ------------------------------------------------------

    for keyword in AKAN_KEYWORDS:

        if keyword in title:
            score += 4

        elif keyword in body:
            score += 1

    return score


# ==========================================================
# EDUCATIONAL RELEVANCE
# ==========================================================

def calculate_educational_relevance(
    result,
):
    """
    Determine how educationally useful
    a result is.
    """

    title = result.get(
        "title",
        "",
    ).lower()

    body = result.get(
        "body",
        "",
    ).lower()

    score = 0

    for keyword in EDUCATIONAL_KEYWORDS:

        if keyword in title:
            score += 3

        elif keyword in body:
            score += 1

    body_length = len(
        body
    )

    if 100 <= body_length <= 700:
        score += 4

    elif 700 < body_length <= 1200:
        score += 2

    elif body_length > 1800:
        score -= 2

    return score


# ==========================================================
# TOTAL RESULT SCORE
# ==========================================================

def calculate_result_score(
    result,
    query,
    akan=False,
):
    """
    Combine:

    - Source quality
    - Query relevance
    - Educational relevance
    - Akan relevance
    """

    source_score = get_source_score(
        result,
        akan=akan,
    )

    query_score = calculate_query_relevance(
        result,
        query,
    )

    educational_score = calculate_educational_relevance(
        result
    )

    akan_score = 0

    if akan:

        akan_score = calculate_akan_relevance(
            result,
            query,
        )

    return (
        source_score
        + query_score
        + educational_score
        + akan_score
    )


# ==========================================================
# SEARCH ONE QUERY
# ==========================================================

def search_web(
    query,
    max_results=8,
    akan=False,
):
    """
    Search the web for one query.
    """

    if not query:
        return []

    try:

        print(
            "🌍 Web Search:",
            query,
        )

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=max_results,
                )
            )

        if not results:
            return []

        for result in results:

            result["_query"] = query

            result["_score"] = calculate_result_score(
                result,
                query,
                akan=akan,
            )

        results.sort(
            key=lambda item: item.get(
                "_score",
                0,
            ),
            reverse=True,
        )

        return results

    except Exception as e:

        print(
            "❌ Web Search Error:",
            e,
        )

        return []


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicate_results(
    results,
):
    """
    Remove duplicate URLs while keeping
    the strongest result.
    """

    if not results:
        return []

    unique = {}

    for result in results:

        url = result.get(
            "href",
            "",
        ).strip()

        if not url:
            continue

        normalized_url = (
            url.lower()
            .rstrip("/")
        )

        current_score = result.get(
            "_score",
            0,
        )

        if normalized_url not in unique:

            unique[
                normalized_url
            ] = result

        else:

            old_score = unique[
                normalized_url
            ].get(
                "_score",
                0,
            )

            if current_score > old_score:

                unique[
                    normalized_url
                ] = result

    return list(
        unique.values()
    )


# ==========================================================
# SEARCH MULTIPLE QUERIES
# ==========================================================

def search_multiple_queries(
    queries,
    max_results_per_query=6,
    akan=False,
):
    """
    Search multiple queries and combine
    all results.
    """

    if not queries:
        return []

    all_results = []

    for query in queries:

        query = str(
            query
        ).strip()

        if not query:
            continue

        results = search_web(
            query,
            max_results=max_results_per_query,
            akan=akan,
        )

        all_results.extend(
            results
        )

    return remove_duplicate_results(
        all_results
    )


# ==========================================================
# RERANK RESULTS
# ==========================================================

def rerank_results(
    results,
    query="",
    akan=False,
):
    """
    Recalculate the final ranking after
    multiple searches.
    """

    if not results:
        return []

    for result in results:

        source_score = get_source_score(
            result,
            akan=akan,
        )

        query_score = 0

        if query:

            query_score = calculate_query_relevance(
                result,
                query,
            )

        educational_score = calculate_educational_relevance(
            result
        )

        akan_score = 0

        if akan:

            akan_score = calculate_akan_relevance(
                result,
                query,
            )

        # --------------------------------------------------
        # Query diversity bonus
        # --------------------------------------------------

        query_bonus = 0

        if result.get(
            "_query",
            "",
        ):

            query_bonus = 2

        result["_final_score"] = (
            source_score
            + query_score
            + educational_score
            + akan_score
            + query_bonus
        )

    results.sort(
        key=lambda item: item.get(
            "_final_score",
            0,
        ),
        reverse=True,
    )

    return results


# ==========================================================
# GET TOP RESULTS
# ==========================================================

def get_top_results(
    results,
    limit=5,
):
    """
    Select strong results while encouraging
    source diversity.
    """

    if not results:
        return []

    selected = []

    seen_domains = set()

    # ------------------------------------------------------
    # First pass
    # ------------------------------------------------------

    for result in results:

        body = result.get(
            "body",
            "",
        ).strip()

        if len(body) < 20:
            continue

        domain = get_domain(
            result.get(
                "href",
                "",
            )
        )

        if domain in seen_domains:
            continue

        selected.append(
            result
        )

        seen_domains.add(
            domain
        )

        if len(selected) >= limit:
            break

    # ------------------------------------------------------
    # Second pass
    # ------------------------------------------------------

    if len(selected) < limit:

        for result in results:

            if result in selected:
                continue

            body = result.get(
                "body",
                "",
            ).strip()

            if len(body) < 20:
                continue

            selected.append(
                result
            )

            if len(selected) >= limit:
                break

    return selected


# ==========================================================
# CLEAN SUMMARY
# ==========================================================

def clean_summary(
    text,
    max_length=700,
):
    """
    Clean and shorten a web result summary.
    """

    if not text:
        return ""

    text = " ".join(
        str(text).split()
    )

    if len(text) > max_length:

        text = (
            text[:max_length]
            .rsplit(
                " ",
                1,
            )[0]
            + "..."
        )

    return text


# ==========================================================
# FORMAT SINGLE RESULT
# ==========================================================

def format_web_result(
    result,
):
    """
    Convert one raw DDGS result into
    structured data.
    """

    if not result:
        return None

    title = result.get(
        "title",
        "No Title",
    )

    body = clean_summary(
        result.get(
            "body",
            "",
        )
    )

    url = result.get(
        "href",
        "",
    )

    domain = get_domain(
        url
    )

    category = get_domain_category(
        domain
    )

    score = result.get(
        "_final_score",
        result.get(
            "_score",
            0,
        ),
    )

    return {
        "title": title,
        "summary": body,
        "url": url,
        "domain": domain,
        "category": category,
        "score": score,
        "source_type": "web",
        "query": result.get(
            "_query",
            "",
        ),
    }


# ==========================================================
# FORMAT MULTIPLE RESULTS
# ==========================================================

def format_web_results(
    results,
):
    """
    Convert multiple raw results.
    """

    formatted = []

    for result in results:

        item = format_web_result(
            result
        )

        if item:

            formatted.append(
                item
            )

    return formatted


# ==========================================================
# UNIQUE QUERY CLEANER
# ==========================================================

def unique_queries(
    queries,
    limit=15,
):
    """
    Remove duplicate search queries.
    """

    cleaned = []

    seen = set()

    for query in queries:

        if not query:
            continue

        query = str(
            query
        ).strip()

        if not query:
            continue

        key = query.lower()

        if key in seen:
            continue

        seen.add(
            key
        )

        cleaned.append(
            query
        )

        if len(cleaned) >= limit:
            break

    return cleaned


# ==========================================================
# AKAN / TWI QUERY BUILDER
# ==========================================================

def build_akan_web_queries(
    term,
    query_type="general",
):
    """
    Build targeted web queries for Akan/Twi.
    """

    term = str(
        term
    ).strip()

    if not term:
        return []

    queries = []

    # ------------------------------------------------------
    # Exact searches
    # ------------------------------------------------------

    queries.extend([
        f'"{term}" Twi',
        f'"{term}" Akan',
        f'"{term}" English',
    ])

    # ------------------------------------------------------
    # Definition
    # ------------------------------------------------------

    if query_type == "definition":

        queries.extend([
            f'"{term}" meaning Twi',
            f'"{term}" meaning Akan',
            f'"{term}" English meaning',
            f'"{term}" Twi dictionary',
            f'"{term}" Akan dictionary',
            f'"{term}" definition Twi',
            f'"{term}" definition Akan',
        ])

    # ------------------------------------------------------
    # Translation
    # ------------------------------------------------------

    elif query_type == "translation":

        queries.extend([
            f'"{term}" English translation',
            f'"{term}" Twi translation',
            f'"{term}" Akan translation',
            f'"{term}" English Twi dictionary',
            f'"{term}" Twi English dictionary',
        ])

    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    elif query_type == "explanation":

        queries.extend([
            f'"{term}" Twi explanation',
            f'"{term}" Akan explanation',
            f'"{term}" meaning and usage Twi',
            f'"{term}" Twi usage',
            f'"{term}" Twi explained',
        ])

    # ------------------------------------------------------
    # Examples
    # ------------------------------------------------------

    elif query_type == "example":

        queries.extend([
            f'"{term}" Twi example',
            f'"{term}" Twi sentence',
            f'"{term}" used in a sentence Twi',
            f'"{term}" Akan sentence',
            f'"{term}" Twi usage example',
        ])

    # ------------------------------------------------------
    # Synonyms
    # ------------------------------------------------------

    elif query_type == "synonym":

        queries.extend([
            f'"{term}" Twi synonyms',
            f'"{term}" Akan synonyms',
            f'"{term}" similar Twi words',
            f'"{term}" related Twi words',
        ])

    # ------------------------------------------------------
    # Antonyms
    # ------------------------------------------------------

    elif query_type == "antonym":

        queries.extend([
            f'"{term}" Twi antonym',
            f'"{term}" Akan antonym',
            f'"{term}" opposite in Twi',
            f'"{term}" opposite meaning Twi',
        ])

    # ------------------------------------------------------
    # Description
    # ------------------------------------------------------

    elif query_type == "description":

        queries.extend([
            f'"{term}" Twi description',
            f'"{term}" Akan description',
            f'"{term}" meaning and description',
            f'"{term}" Twi usage',
        ])

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    else:

        queries.extend([
            f'"{term}" Twi meaning',
            f'"{term}" Akan meaning',
            f'"{term}" Twi usage',
            f'"{term}" Twi example',
            f'"{term}" English meaning',
        ])

    # ------------------------------------------------------
    # Specialist dictionary searches
    # ------------------------------------------------------

    queries.extend([
        f'"{term}" site:akandictionary.com',
        f'"{term}" site:glosbe.com',
        f'"{term}" site:afiaghana.com',
        f'"{term}" site:learnakan.com',
    ])

    return unique_queries(
        queries,
        limit=15,
    )


# ==========================================================
# SEARCH AKAN / TWI WEB
# ==========================================================

def search_akan_web(
    term,
    query_type="general",
    limit=5,
):
    """
    Dynamic Akan/Twi web retrieval.

    Searches dictionary, translation,
    educational and NLP sources.
    """

    if not term:
        return []

    print(
        "\n🇬🇭 AKAN/TWI WEB RETRIEVAL"
    )

    print(
        "Target:",
        term,
    )

    print(
        "Request:",
        query_type,
    )

    queries = build_akan_web_queries(
        term,
        query_type,
    )

    print(
        "Akan Web Queries:",
        len(queries),
    )

    results = search_multiple_queries(
        queries,
        max_results_per_query=5,
        akan=True,
    )

    if not results:

        print(
            "⚠️ No Akan/Twi web results."
        )

        return []

    results = rerank_results(
        results,
        term,
        akan=True,
    )

    results = get_top_results(
        results,
        limit=limit,
    )

    formatted = format_web_results(
        results
    )

    # ------------------------------------------------------
    # Add Akan metadata
    # ------------------------------------------------------

    for item in formatted:

        item["language"] = "akan"

        item["target"] = term

        item["query_type"] = query_type

    print(
        "🇬🇭 Akan Web Results:",
        len(formatted),
    )

    return formatted


# ==========================================================
# GENERAL EDUCATIONAL QUERY BUILDER
# ==========================================================

def generate_educational_queries(
    question,
):
    """
    Generate educational search variants.
    """

    question = str(
        question
    ).strip()

    if not question:
        return []

    queries = [
        question,
        f"{question} definition",
        f"{question} explained",
        f"{question} educational explanation",
        f"{question} examples",
        f"{question} textbook",
        f"{question} lecture notes",
        f"{question} site:openstax.org",
        f"{question} site:ocw.mit.edu",
    ]

    return unique_queries(
        queries,
        limit=12,
    )


# ==========================================================
# EDUCATIONAL WEB RETRIEVAL
# ==========================================================

def search_educational_web(
    queries,
):
    """
    Search the educational web.

    Accepts either:
        a string
    or:
        a list of queries.
    """

    if isinstance(
        queries,
        str,
    ):

        queries = [
            queries
        ]

    if not queries:
        return []

    results = search_multiple_queries(
        queries,
        max_results_per_query=6,
        akan=False,
    )

    if not results:
        return []

    original_query = queries[0]

    results = rerank_results(
        results,
        original_query,
        akan=False,
    )

    results = get_top_results(
        results,
        limit=5,
    )

    return format_web_results(
        results
    )


# ==========================================================
# FORMAT MULTI-SOURCE RESPONSE
# ==========================================================

def format_multi_source_response(
    results,
):
    """
    Create a concise response from
    multiple web sources.
    """

    if not results:
        return None

    if (
        isinstance(
            results[0],
            dict,
        )
        and "summary" in results[0]
    ):

        formatted = results

    else:

        formatted = format_web_results(
            results
        )

    if not formatted:
        return None

    answer_parts = []

    for item in formatted:

        summary = item.get(
            "summary",
            "",
        )

        if summary:

            answer_parts.append(
                summary
            )

    if not answer_parts:
        return None

    # ------------------------------------------------------
    # Remove duplicate summaries
    # ------------------------------------------------------

    unique_summaries = []

    seen = set()

    for summary in answer_parts:

        normalized = (
            summary
            .lower()
            .strip()
        )

        if normalized in seen:
            continue

        seen.add(
            normalized
        )

        unique_summaries.append(
            summary
        )

    unique_summaries = (
        unique_summaries[:3]
    )

    answer = " ".join(
        unique_summaries
    )

    # ------------------------------------------------------
    # Sources
    # ------------------------------------------------------

    source_domains = []

    for item in formatted:

        domain = item.get(
            "domain",
            "",
        )

        if (
            domain
            and domain not in source_domains
        ):

            source_domains.append(
                domain
            )

    source_text = ", ".join(
        source_domains[:5]
    )

    return (
        "🌍 Multi-Source Web Knowledge\n\n"
        + answer
        + "\n\n"
        + "Sources: "
        + source_text
    )


# ==========================================================
# GENERAL SEARCH + FORMAT
# ==========================================================

def search_and_format(
    query,
):
    """
    Compatibility function for
    existing router code.
    """

    results = search_web(
        query,
        max_results=8,
    )

    results = rerank_results(
        results,
        query,
    )

    results = get_top_results(
        results,
        limit=3,
    )

    return format_multi_source_response(
        results
    )


# ==========================================================
# SEARCH AND SUMMARIZE
# ==========================================================

def search_and_summarize(
    queries,
):
    """
    Search educational sources and
    create a concise multi-source response.
    """

    results = search_educational_web(
        queries
    )

    if not results:
        return None

    return format_multi_source_response(
        results
    )


# ==========================================================
# TEST AKAN WEB ENGINE
# ==========================================================

def test_akan_web_engine():
    """
    Test dynamic Akan/Twi retrieval.
    """

    tests = [

        (
            "nsuo",
            "definition",
        ),

        (
            "ɔdɔ",
            "definition",
        ),

        (
            "akwaaba",
            "translation",
        ),

        (
            "sukuu",
            "explanation",
        ),

        (
            "nsuo retɔ",
            "definition",
        ),

    ]

    print(
        "\n=========================================="
    )

    print(
        "🇬🇭 AKAN/TWI WEB ENGINE TEST"
    )

    print(
        "=========================================="
    )

    for term, query_type in tests:

        print(
            "\n------------------------------------------"
        )

        print(
            "TERM:",
            term,
        )

        print(
            "TYPE:",
            query_type,
        )

        results = search_akan_web(
            term,
            query_type,
            limit=5,
        )

        print(
            "\nRESULTS:",
            len(results),
        )

        for index, result in enumerate(
            results,
            start=1,
        ):

            print(
                f"\n{index}. "
                + result.get(
                    "title",
                    "",
                )
            )

            print(
                "Domain:",
                result.get(
                    "domain",
                    "",
                )
            )

            print(
                "Category:",
                result.get(
                    "category",
                    "",
                )
            )

            print(
                "Score:",
                result.get(
                    "score",
                    0,
                )
            )

            print(
                "Summary:",
                result.get(
                    "summary",
                    "",
                )
            )

            print(
                "URL:",
                result.get(
                    "url",
                    "",
                )
            )


# ==========================================================
# TEST GENERAL WEB ENGINE
# ==========================================================

def test_web_engine():
    """
    Test general educational web retrieval.
    """

    tests = [
        "artificial intelligence definition",
        "machine learning explained",
        "computer networks",
    ]

    print(
        "\n=========================================="
    )

    print(
        "🌍 GENERAL WEB ENGINE TEST"
    )

    print(
        "=========================================="
    )

    for query in tests:

        print(
            "\n------------------------------------------"
        )

        print(
            "QUERY:",
            query,
        )

        results = search_educational_web(
            [query]
        )

        print(
            "RESULTS:",
            len(results),
        )

        for index, result in enumerate(
            results,
            start=1,
        ):

            print(
                f"{index}. "
                + result.get(
                    "title",
                    "",
                )
                + " | "
                + result.get(
                    "domain",
                    "",
                )
            )


# ==========================================================
# DIRECT EXECUTION
# ==========================================================

if __name__ == "__main__":

    test_akan_web_engine()

    test_web_engine()


# ==========================================================
# END OF WEB ENGINE
# ==========================================================