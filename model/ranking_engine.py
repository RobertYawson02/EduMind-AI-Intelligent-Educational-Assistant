"""Transparent TF-IDF/cosine answer-ranking engine.

The ranking model keeps the existing engine API while making the score easier
to explain in a final-year project: every candidate receives a 0-100 score
from source reliability, semantic relevance, topic fit, intent fit, quality,
structure, conciseness, and (for web/dataset results) external evidence.
"""

import re
from urllib.parse import urlparse

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    TfidfVectorizer = None
    cosine_similarity = None
    SKLEARN_AVAILABLE = False

SOURCE_PRIORITY = {
    "knowledge": 20,
    "akan": 20,
    "ghana_qa": 18,
    "ghana_qa_sample": 16,
    "educational_web": 15,
    "web": 9,
    "unknown": 4,
}

TRUSTED_DOMAINS = {
    "openstax.org", "ocw.mit.edu", "mit.edu", "khanacademy.org",
    "britannica.com", "stanford.edu", "harvard.edu", "coursera.org",
    "ibm.com", "microsoft.com", "oracle.com", "aws.amazon.com",
    "nist.gov", "cisco.com", "python.org", "scikit-learn.org",
    "huggingface.co", "ghananlp.org",
}
GENERAL_DOMAINS = {"wikipedia.org"}
LOW_TRUST_DOMAINS = {"example.com", "example.org", "example.net"}

INTENT_MARKERS = {
    "definition": ["is defined as", "refers to", "means", "is a", "is an", "is the ability"],
    "meaning": ["means", "refers to", "meaning"],
    "advantages": ["advantages", "benefits", "benefit", "positive", "importance"],
    "disadvantages": ["disadvantages", "limitations", "drawbacks", "problems", "negative"],
    "applications": ["applications", "used in", "used for", "applied", "used to"],
    "examples": ["examples", "such as", "include", "for instance"],
    "list": ["types", "include", "1.", "2.", "3.", "first", "second"],
    "causes": ["causes", "because", "reasons", "reason"],
    "effects": ["effects", "impact", "results", "consequences"],
    "comparison": ["difference", "whereas", "while", "both", "however", "compared"],
    "process": ["steps", "first", "then", "next", "finally", "process"],
    "calculation": ["=", "formula", "solution", "therefore"],
    "translation": ["translate", "translation", "in twi", "into twi", "akan"],
    "summary": ["summary", "summarize", "summarise", "overall", "briefly"],
    "exam": ["definition", "key points", "examples", "important", "advantages", "disadvantages"],
    "explanation": ["because", "works by", "involves", "this means", "explains"],
}

STOPWORDS = {
    "what","is","are","the","a","an","of","to","in","on","for","and","or",
    "how","why","can","could","would","should","does","do","did","i","me","my",
    "we","you","your","please","tell","about","give","explain","describe","this",
    "that","these","those","it","its","was","were","be","been","being","from","with",
    "as","at","by","into","than","between","there","their","they",
}

EDUCATIONAL_WORDS = {
    "student","students","education","learning","study","academic","school","university",
    "college","course","lesson","textbook","chapter","concept","principle","theory",
    "example","definition","explanation","lecture","notes","examination","exam","revision",
    "knowledge","computer","technology","science","system","method","process","model",
}


def clean_text(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


def tokenize(text):
    words = re.findall(r"[a-zA-ZÀ-ÿɔɛƆƐ0-9]+", clean_text(text).lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]


def get_question_words(question):
    return tokenize(question)


def get_topic_words(topic):
    return tokenize(topic)


def calculate_token_overlap(question, answer):
    q = set(tokenize(question))
    a = set(tokenize(answer))
    return len(q & a) / len(q) if q else 0.0


def calculate_tfidf_similarity(question, answer):
    if not question or not answer:
        return 0.0
    if not SKLEARN_AVAILABLE:
        return calculate_token_overlap(question, answer)
    try:
        vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), sublinear_tf=True)
        matrix = vectorizer.fit_transform([clean_text(question), clean_text(answer)])
        return float(max(0.0, min(1.0, cosine_similarity(matrix[0:1], matrix[1:2])[0][0])))
    except Exception:
        return calculate_token_overlap(question, answer)


def calculate_question_relevance(question, answer):
    similarity = calculate_tfidf_similarity(question, answer)
    overlap = calculate_token_overlap(question, answer)
    return round((similarity * 0.70 + overlap * 0.30) * 30, 2)


def calculate_topic_relevance(topic, answer):
    if not topic or not answer:
        return 0.0
    similarity = calculate_tfidf_similarity(topic, answer)
    topic_tokens = set(tokenize(topic))
    answer_tokens = set(tokenize(answer))
    overlap = len(topic_tokens & answer_tokens) / len(topic_tokens) if topic_tokens else 0.0
    exact_phrase = 1.0 if clean_text(topic).lower() in clean_text(answer).lower() else 0.0
    combined = similarity * 0.35 + overlap * 0.35 + exact_phrase * 0.30
    return round(min(15.0, combined * 15), 2)


def calculate_intent_relevance(intent, answer):
    markers = INTENT_MARKERS.get(str(intent or "").lower(), [])
    if not markers or not answer:
        return 0.0
    text = answer.lower()
    hits = sum(1 for marker in markers if marker in text)
    return round(min(15.0, (hits / len(markers)) * 15.0), 2)


def calculate_exam_relevance(question, answer):
    q = set(tokenize(question))
    exam_terms = {"define","definition","explain","describe","discuss","state","list","identify","mention","outline","differentiate","difference","compare","advantages","disadvantages","importance","functions","characteristics","types","causes","effects","steps","process","examples","applications"}
    signal = len(q & exam_terms)
    if not signal:
        return 0.0
    structure_terms = ["definition", "examples", "advantages", "disadvantages", "types", "functions", "applications", "steps", "causes", "effects", "conclusion"]
    answer_hits = sum(1 for x in structure_terms if x in str(answer).lower())
    return round(min(8.0, signal * 2 + min(answer_hits, 4) * 0.5), 2)


def calculate_educational_relevance(answer):
    return round(min(8.0, len(set(tokenize(answer)) & EDUCATIONAL_WORDS) * 0.8), 2)


def calculate_structure_quality(answer):
    text = clean_text(answer)
    if not text:
        return 0.0
    score = 0.0
    if len(re.findall(r"[.!?]", text)) >= 2:
        score += 2
    if re.search(r"(^|\s)\d+[.)]", text):
        score += 2
    if re.search(r"(^|\n)[-•]", text):
        score += 1.5
    if ":" in text:
        score += 1
    if len(text) >= 120:
        score += 1.5
    return min(7.0, score)


def calculate_answer_quality(answer):
    text = clean_text(answer)
    if not text:
        return 0.0
    if re.search(r"error|exception|failed|not found", text.lower()):
        return 0.0
    score = 1.0
    if len(text) >= 50: score += 1.5
    if len(text) >= 100: score += 1.5
    if re.search(r"[.!?]", text): score += 1.5
    if len(text.split()) >= 10: score += 1.5
    return min(7.0, score)


def calculate_conciseness(answer):
    n = len(clean_text(answer))
    if 100 <= n <= 800:
        return 4.0
    if 70 <= n < 100 or 800 < n <= 1100:
        return 3.0
    if 40 <= n < 70:
        return 2.0
    if n < 40:
        return 1.0
    return 0.5


def extract_domain(url):
    try:
        return urlparse(str(url or "")).netloc.lower().split(":")[0].removeprefix("www.")
    except Exception:
        return ""


def get_web_result_text(item):
    if not isinstance(item, dict):
        return ""
    fields = ["summary", "body", "snippet", "description", "text"]
    return clean_text(" ".join(str(item.get(f, "")) for f in fields if item.get(f)))


def get_web_result_url(item):
    if not isinstance(item, dict):
        return ""
    return str(item.get("url") or item.get("href") or item.get("link") or "")


def get_web_result_domain(item):
    if not isinstance(item, dict):
        return ""
    return clean_text(item.get("domain", "")) or extract_domain(get_web_result_url(item))


def calculate_web_source_quality(text, url="", domain=""):
    d = (domain or extract_domain(url)).lower()
    if d in LOW_TRUST_DOMAINS:
        return 0.0
    if d in TRUSTED_DOMAINS or any(d.endswith("." + x) for x in TRUSTED_DOMAINS):
        return 8.0
    if d in GENERAL_DOMAINS:
        return 3.0
    if ".edu" in d or ".ac." in d:
        return 8.0
    return 1.0


def calculate_external_score(item):
    if not isinstance(item, dict):
        return 0.0
    try:
        return min(3.0, max(0.0, float(item.get("score", 0)) * 0.3))
    except (TypeError, ValueError):
        return 0.0


def detect_source_type(source, text="", url="", domain=""):
    source = str(source or "").lower().strip()
    if source in SOURCE_PRIORITY:
        return source
    d = (domain or extract_domain(url)).lower()
    if d in TRUSTED_DOMAINS or ".edu" in d or ".ac." in d:
        return "educational_web"
    return "web"


def calculate_score(source, answer, question="", topic="", intent="", metadata=None):
    if not answer:
        return 0
    metadata = metadata if isinstance(metadata, dict) else {}
    source = detect_source_type(source, answer, metadata.get("url", ""), metadata.get("domain", ""))

    score = SOURCE_PRIORITY.get(source, SOURCE_PRIORITY["unknown"])
    score += calculate_question_relevance(question, answer)
    score += calculate_topic_relevance(topic, answer)
    score += calculate_intent_relevance(intent, answer)
    score += calculate_educational_relevance(answer)
    score += calculate_exam_relevance(question, answer)
    score += calculate_answer_quality(answer)
    score += calculate_structure_quality(answer)
    score += calculate_conciseness(answer)

    if source in {"web", "educational_web"}:
        score += calculate_web_source_quality(answer, metadata.get("url", ""), metadata.get("domain", ""))
        score += calculate_external_score(metadata)
    elif source in {"ghana_qa", "ghana_qa_sample"}:
        try:
            score += min(5.0, max(0.0, float(metadata.get("dataset_score", 0)) * 5.0))
        except (TypeError, ValueError):
            pass

    if "retrieval_score" in metadata:
        try:
            score += min(5.0, max(0.0, float(metadata.get("retrieval_score", 0)) * 5.0))
        except (TypeError, ValueError):
            pass

    requested_language = str(metadata.get("requested_language", "english")).lower()
    candidate_language = str(metadata.get("language", "")).lower()
    if candidate_language and requested_language and candidate_language == requested_language:
        score += 2.0

    return int(round(min(100.0, max(0.0, score))))


def prepare_candidate(source, answer, question="", topic="", intent="", metadata=None):
    answer_text = clean_text(answer)
    if not answer_text:
        return None
    metadata = dict(metadata or {})
    metadata.setdefault("language", "akan" if source == "akan" else "english")
    score = calculate_score(source, answer_text, question, topic, intent, metadata)
    return {
        "source": source,
        "answer": answer_text,
        "score": score,
        "similarity": round(calculate_tfidf_similarity(question, answer_text), 4),
        **{k: v for k, v in metadata.items() if k in {"title","url","domain","dataset_question","dataset_score","language"}},
    }


def rank_web_result(item, question="", topic="", intent=""):
    if not isinstance(item, dict):
        return None
    text = get_web_result_text(item)
    if not text:
        return None
    return prepare_candidate(
        detect_source_type("web", text, get_web_result_url(item), get_web_result_domain(item)),
        text,
        question,
        topic,
        intent,
        {
            "title": clean_text(item.get("title", "")),
            "url": get_web_result_url(item),
            "domain": get_web_result_domain(item),
            "score": item.get("score", 0),
            "language": "english",
            "requested_language": "english",
        },
    )


def are_similar_answers(answer_one, answer_two, threshold=0.90):
    return calculate_tfidf_similarity(answer_one, answer_two) >= threshold if answer_one and answer_two else False


def remove_duplicate_candidates(candidates):
    unique = []
    for candidate in sorted(candidates, key=lambda x: (x.get("score", 0), x.get("similarity", 0)), reverse=True):
        if not any(are_similar_answers(candidate.get("answer", ""), existing.get("answer", "")) for existing in unique):
            unique.append(candidate)
    return unique


def collect_candidates(results, question="", topic="", intent=""):
    candidates = []
    if not results:
        return candidates

    metadata_keys = {"question","topic","intent","query_type","language","is_akan","target","sources"}
    for source, answer in results.items():
        if source in metadata_keys or not answer:
            continue

        if source in {"ghana_qa", "ghana_qa_sample"}:
            items = answer if isinstance(answer, list) else [answer]
            for item in items:
                if isinstance(item, dict) and item.get("answer"):
                    c = prepare_candidate(
                        source, item["answer"], question, topic, intent,
                        {"dataset_question": item.get("question", ""), "dataset_score": item.get("score", 0), "language": item.get("language", ""), "requested_language": "akan" if results.get("is_akan") else "english"},
                    )
                    if c: candidates.append(c)
            continue

        if source in {"web", "educational_web"}:
            items = answer if isinstance(answer, list) else [answer]
            for item in items:
                if isinstance(item, dict):
                    c = rank_web_result(item, question, topic, intent)
                    if c: candidates.append(c)
                elif isinstance(item, str):
                    c = prepare_candidate(source, item, question, topic, intent)
                    if c: candidates.append(c)
            continue

        if isinstance(answer, dict):
            text = answer.get("answer", "")
            if text:
                c = prepare_candidate(
                    source, text, question, topic, intent,
                    {
                        "requested_language": "akan" if results.get("is_akan") else "english",
                        "retrieval_score": answer.get("retrieval_score", 0.0),
                    },
                )
                if c: candidates.append(c)
            continue

        if isinstance(answer, str):
            c = prepare_candidate(source, answer, question, topic, intent, {"requested_language": "akan" if results.get("is_akan") else "english"})
            if c: candidates.append(c)

    return candidates


def rank_answers(results, question="", topic="", intent=""):
    candidates = remove_duplicate_candidates(collect_candidates(results, question, topic, intent))
    if not candidates:
        return None
    candidates.sort(key=lambda x: (x.get("score", 0), x.get("similarity", 0), -len(x.get("answer", ""))), reverse=True)
    print("\n======================================")
    print("🏆 RANKING RESULTS")
    print("======================================")
    for i, item in enumerate(candidates[:10], 1):
        print(f"{i}. {item.get('source', 'unknown')} → {item.get('score', 0)} | similarity={item.get('similarity', 0)}")
        if item.get("domain"): print(f"   Domain: {item['domain']}")
    return candidates[0]


def get_top_answers(results, question="", topic="", intent="", limit=3):
    if limit <= 0:
        return []
    candidates = remove_duplicate_candidates(collect_candidates(results, question, topic, intent))
    candidates.sort(key=lambda x: (x.get("score", 0), x.get("similarity", 0)), reverse=True)
    return candidates[:limit]


def combine_ranked_answers(results, question="", topic="", intent=""):
    best = rank_answers(results, question, topic, intent)
    return best.get("answer") if best else None


def ranking_confidence(ranked_answers):
    """Return an interpretable 0-1 confidence from top score and score margin."""
    if not ranked_answers:
        return 0.0
    scores = [float(x.get("score", 0)) for x in ranked_answers if isinstance(x, dict)]
    if not scores:
        return 0.0
    top = min(100.0, max(0.0, scores[0])) / 100.0
    margin = 0.0
    if len(scores) > 1:
        margin = min(1.0, max(0.0, (scores[0] - scores[1]) / 25.0))
    return round(min(1.0, top * 0.75 + margin * 0.25), 2)


if __name__ == "__main__":
    sample = {
        "knowledge": "Artificial intelligence is the ability of computer systems to perform tasks that normally require human intelligence. It can learn from data, understand language, solve problems and support decisions.",
        "web": [{"title": "Artificial Intelligence", "body": "AI enables computer systems to perform tasks associated with human intelligence.", "href": "https://example.com/ai"}],
        "akan": "Artificial intelligence yɛ computer technology a ɛboa mfiri ma wɔyɛ nneɛma bi a nnipa tumi yɛ.",
    }
    ranked = get_top_answers(sample, "What are the applications of artificial intelligence?", "artificial intelligence", "applications", 3)
    for i, item in enumerate(ranked, 1):
        print(i, item)
