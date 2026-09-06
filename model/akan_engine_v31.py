# model/akan_engine_v31.py
"""
Akan Knowledge Engine V3.1

Purpose
-------
Intelligent Akan/Twi educational and general-knowledge retrieval layer.

V3.1 improvements:
- Reliable request-type detection
- Exact whole-word matching
- Translation target extraction
- Meaning/definition detection
- Related-word detection
- Synonym and antonym support
- Example retrieval
- Semantic fallback
- Confidence scoring
- Compatibility-oriented response structure
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class AkanEngine:
    """Intelligent retrieval engine for the Akan knowledge base."""

    VERSION = "3.1"

    def __init__(self, knowledge_base_path: Optional[str] = None):
        root = Path(__file__).resolve().parent.parent

        if knowledge_base_path:
            self.knowledge_base_path = Path(knowledge_base_path)
        else:
            self.knowledge_base_path = (
                root / "data" / "akan" / "akan_knowledge_base.json"
            )

        self.records: List[Dict[str, Any]] = []
        self._load_knowledge_base()

    # ------------------------------------------------------------------
    # Knowledge-base loading
    # ------------------------------------------------------------------

    def _load_knowledge_base(self) -> None:
        """Load the Akan knowledge base safely."""

        if not self.knowledge_base_path.exists():
            self.records = []
            return

        try:
            with self.knowledge_base_path.open(
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            if isinstance(data, list):
                self.records = data

            elif isinstance(data, dict):
                for key in (
                    "records",
                    "entries",
                    "knowledge",
                    "data",
                    "items",
                ):
                    if isinstance(data.get(key), list):
                        self.records = data[key]
                        break
                else:
                    self.records = []

            else:
                self.records = []

        except (json.JSONDecodeError, OSError):
            self.records = []

    # ------------------------------------------------------------------
    # Text normalization
    # ------------------------------------------------------------------

    @staticmethod
    def normalize_text(text: Any) -> str:
        """Normalize text while preserving Akan characters."""

        if text is None:
            return ""

        text = str(text).lower().strip()

        text = re.sub(r"[“”\"'`]", "", text)
        text = re.sub(r"[?!.,;:()\[\]{}]", " ", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def tokenize(text: Any) -> List[str]:
        """Return whole-word tokens."""

        normalized = AkanEngine.normalize_text(text)

        if not normalized:
            return []

        return re.findall(
            r"\b[\wÀ-ÖØ-öø-ÿƐɛƆɔĀāĒēĪīŌōŪū]+\b",
            normalized,
            flags=re.UNICODE,
        )

    @staticmethod
    def contains_phrase(text: str, phrase: str) -> bool:
        """
        Whole-word / phrase matching.

        This intentionally avoids substring matching.

        Example:
            'to' does NOT match 'school'.
        """

        text = AkanEngine.normalize_text(text)
        phrase = AkanEngine.normalize_text(phrase)

        if not text or not phrase:
            return False

        pattern = r"(?<!\w)" + re.escape(phrase) + r"(?!\w)"

        return re.search(pattern, text, flags=re.UNICODE) is not None

    # ------------------------------------------------------------------
    # Record field handling
    # ------------------------------------------------------------------

    @staticmethod
    def _field(record: Dict[str, Any], *names: str) -> Any:
        """Return the first populated field among possible schema names."""

        for name in names:
            value = record.get(name)

            if value is not None and value != "":
                return value

        return None

    @staticmethod
    def _as_list(value: Any) -> List[str]:
        """Convert a scalar/list field into a clean string list."""

        if value is None:
            return []

        if isinstance(value, list):
            return [
                str(item).strip()
                for item in value
                if item is not None and str(item).strip()
            ]

        if isinstance(value, str):
            parts = re.split(r"[,;|]", value)

            return [
                part.strip()
                for part in parts
                if part.strip()
            ]

        return [str(value).strip()]

    def _record_words(self, record: Dict[str, Any]) -> List[str]:
        """Collect searchable words from a record."""

        fields = [
            "word",
            "term",
            "akan",
            "twi",
            "english",
            "translation",
            "meaning",
            "definition",
            "topic",
            "category",
        ]

        words: List[str] = []

        for field in fields:
            value = record.get(field)

            if isinstance(value, str):
                words.append(value)

            elif isinstance(value, list):
                words.extend(str(item) for item in value)

        for field in (
            "keywords",
            "synonyms",
            "antonyms",
            "related_words",
            "related_terms",
        ):
            words.extend(self._as_list(record.get(field)))

        return words

    # ------------------------------------------------------------------
    # Request detection
    # ------------------------------------------------------------------

    def detect_request_type(self, query: str) -> str:
        """
        Detect what the user wants.

        Priority matters because a query may contain several trigger words.
        """

        q = self.normalize_text(query)

        # --------------------------------------------------------------
        # 1. Explicit translation request
        # --------------------------------------------------------------

        translation_patterns = [
            r"\btranslate\b",
            r"\btranslation\b",
            r"\bhow do you say\b",
            r"\bhow do i say\b",
            r"\bwhat is .* in twi\b",
            r"\bwhat is .* in akan\b",
            r"\bhow is .* said in twi\b",
            r"\bhow is .* said in akan\b",
        ]

        if any(re.search(pattern, q) for pattern in translation_patterns):
            return "translation"

        # --------------------------------------------------------------
        # 2. Synonyms
        # --------------------------------------------------------------

        synonym_patterns = [
            r"\bsynonym\b",
            r"\bsynonyms\b",
            r"\bwords similar to\b",
            r"\bword similar to\b",
            r"\bsimilar words\b",
            r"\bother words for\b",
        ]

        if any(re.search(pattern, q) for pattern in synonym_patterns):
            return "synonym"

        # --------------------------------------------------------------
        # 3. Antonyms
        # --------------------------------------------------------------

        antonym_patterns = [
            r"\bantonym\b",
            r"\bantonyms\b",
            r"\bopposite word\b",
            r"\bopposite words\b",
            r"\bopposite of\b",
            r"\bwords opposite to\b",
        ]

        if any(re.search(pattern, q) for pattern in antonym_patterns):
            return "antonym"

        # --------------------------------------------------------------
        # 4. Related words
        # --------------------------------------------------------------

        related_patterns = [
            r"\brelated words\b",
            r"\brelated word\b",
            r"\brelated terms\b",
            r"\bwords related to\b",
            r"\bword related to\b",
            r"\bwords associated with\b",
            r"\bassociated words\b",
        ]

        if any(re.search(pattern, q) for pattern in related_patterns):
            return "related"

        # --------------------------------------------------------------
        # 5. Examples
        # --------------------------------------------------------------

        example_patterns = [
            r"\bexample\b",
            r"\bexamples\b",
            r"\buse .* in a sentence\b",
            r"\buse .* in sentences\b",
            r"\bgive me a sentence\b",
            r"\bgive me sentences\b",
        ]

        if any(re.search(pattern, q) for pattern in example_patterns):
            return "example"

        # --------------------------------------------------------------
        # 6. Meaning / definition
        # --------------------------------------------------------------

        meaning_patterns = [
            r"\bwhat does .* mean\b",
            r"\bwhat do .* mean\b",
            r"\bmeaning of\b",
            r"\bdefinition of\b",
            r"\bdefine\b",
            r"\bexplain the meaning of\b",
            r"\bwhat is the meaning\b",
            r"\bkyerɛ dɛn\b",
            r"\bkyere den\b",
            r"\bɛyɛ dɛn\b",
        ]

        if any(re.search(pattern, q) for pattern in meaning_patterns):
            return "meaning"

        # --------------------------------------------------------------
        # 7. Education / explanation
        # --------------------------------------------------------------

        education_patterns = [
            r"\bwhat is\b",
            r"\bwhat are\b",
            r"\bexplain\b",
            r"\bdescribe\b",
            r"\bhow does\b",
            r"\bhow do\b",
            r"\bwhy does\b",
            r"\bwhy do\b",
            r"\bdefine\b",
        ]

        if any(re.search(pattern, q) for pattern in education_patterns):
            return "education"

        return "general"

    # ------------------------------------------------------------------
    # Extract target word / phrase
    # ------------------------------------------------------------------

    def extract_translation_target(self, query: str) -> str:
        """
        Extract the English/Akan word or phrase being translated.

        Important:
        'Translate water into Twi'
        returns 'water', not 'twi'.
        """

        q = self.normalize_text(query)

        patterns = [
            r"translate\s+(.+?)\s+(?:into|to)\s+(?:twi|akan|akan language)$",
            r"translate\s+(.+?)\s+(?:into|to)\s+(?:the\s+)?(?:twi|akan)$",
            r"how\s+do\s+(?:you|i)\s+say\s+(.+?)\s+in\s+(?:twi|akan)$",
            r"how\s+is\s+(.+?)\s+said\s+in\s+(?:twi|akan)$",
            r"what\s+is\s+(.+?)\s+in\s+(?:twi|akan)$",
            r"(.+?)\s+in\s+(?:twi|akan)$",
        ]

        for pattern in patterns:
            match = re.search(pattern, q)

            if match:
                target = match.group(1).strip()

                # Remove common request prefixes.
                target = re.sub(
                    r"^(the\s+)?word\s+",
                    "",
                    target,
                ).strip()

                if target:
                    return target

        # Fallback for "translate water"
        match = re.search(
            r"^translate\s+(.+)$",
            q,
        )

        if match:
            return match.group(1).strip()

        return ""

    def extract_target_word(self, query: str) -> str:
        """Extract the likely target word for non-translation requests."""

        q = self.normalize_text(query)

        patterns = [
            r"meaning\s+of\s+(.+)$",
            r"definition\s+of\s+(.+)$",
            r"what\s+does\s+(.+?)\s+mean",
            r"what\s+do\s+(.+?)\s+mean",
            r"define\s+(.+)$",
            r"synonyms?\s+(?:for|of)\s+(.+)$",
            r"antonyms?\s+(?:for|of)\s+(.+)$",
            r"opposite\s+of\s+(.+)$",
            r"related\s+(?:words?|terms?)\s+(?:to|for)\s+(.+)$",
            r"words?\s+related\s+to\s+(.+)$",
            r"examples?\s+(?:of|for)\s+(.+)$",
        ]

        for pattern in patterns:
            match = re.search(pattern, q)

            if match:
                value = match.group(1).strip()

                value = re.sub(
                    r"\s+(?:in|using)\s+(?:twi|akan)$",
                    "",
                    value,
                ).strip()

                return value

        return ""

    # ------------------------------------------------------------------
    # Matching
    # ------------------------------------------------------------------

    def _exact_matches(
        self,
        target: str,
    ) -> List[Tuple[Dict[str, Any], int]]:
        """Find records with exact whole-word/phrase matches."""

        target = self.normalize_text(target)

        if not target:
            return []

        results: List[Tuple[Dict[str, Any], int]] = []

        for record in self.records:
            score = 0

            primary_fields = [
                "word",
                "term",
                "akan",
                "twi",
                "english",
                "translation",
            ]

            for field in primary_fields:
                value = record.get(field)

                if isinstance(value, str):
                    if self.contains_phrase(value, target):
                        score += 100

                        if self.normalize_text(value) == target:
                            score += 50

            for field in (
                "keywords",
                "synonyms",
                "antonyms",
                "related_words",
                "related_terms",
            ):
                for value in self._as_list(record.get(field)):
                    if self.contains_phrase(value, target):
                        score += 60

                        if self.normalize_text(value) == target:
                            score += 20

            if score:
                results.append((record, score))

        results.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        return results

    def _query_overlap_score(
        self,
        query: str,
        record: Dict[str, Any],
    ) -> int:
        """Calculate simple lexical relevance."""

        query_tokens = set(self.tokenize(query))

        if not query_tokens:
            return 0

        record_tokens = set(
            token
            for value in self._record_words(record)
            for token in self.tokenize(value)
        )

        if not record_tokens:
            return 0

        overlap = query_tokens.intersection(record_tokens)

        return len(overlap) * 8

    def _rank_records(
        self,
        query: str,
        candidates: Optional[List[Tuple[Dict[str, Any], int]]] = None,
    ) -> List[Tuple[Dict[str, Any], int]]:
        """Rank records using exact and lexical relevance."""

        if candidates is None:
            candidates = [
                (record, 0)
                for record in self.records
            ]

        ranked: List[Tuple[Dict[str, Any], int]] = []

        for record, base_score in candidates:
            score = base_score

            score += self._query_overlap_score(
                query,
                record,
            )

            category = self.normalize_text(
                self._field(
                    record,
                    "category",
                    "type",
                    "knowledge_type",
                ) or ""
            )

            query_normalized = self.normalize_text(query)

            if category and self.contains_phrase(
                query_normalized,
                category,
            ):
                score += 15

            ranked.append(
                (record, score)
            )

        ranked.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        return ranked

    # ------------------------------------------------------------------
    # Response construction
    # ------------------------------------------------------------------

    def _record_response(
        self,
        record: Dict[str, Any],
        request_type: str,
        score: int,
    ) -> Dict[str, Any]:
        """Create a stable response dictionary."""

        word = self._field(
            record,
            "word",
            "term",
            "akan",
            "twi",
        )

        english = self._field(
            record,
            "english",
            "translation",
            "english_translation",
        )

        meaning = self._field(
            record,
            "meaning",
            "definition",
            "explanation",
            "description",
        )

        examples = self._as_list(
            self._field(
                record,
                "examples",
                "example",
                "sentences",
            )
        )

        synonyms = self._as_list(
            self._field(
                record,
                "synonyms",
                "synonym",
            )
        )

        antonyms = self._as_list(
            self._field(
                record,
                "antonyms",
                "antonym",
            )
        )

        related = self._as_list(
            self._field(
                record,
                "related_words",
                "related_terms",
                "related",
            )
        )

        if request_type == "translation":
            answer = (
                f"{english}"
                if english
                else str(word or meaning or "")
            )

        elif request_type == "synonym":
            answer = (
                ", ".join(synonyms)
                if synonyms
                else (
                    f"No explicit synonyms are available for "
                    f"{word or 'that word'} in the current Akan knowledge base."
                )
            )

        elif request_type == "antonym":
            answer = (
                ", ".join(antonyms)
                if antonyms
                else (
                    f"No explicit antonyms are available for "
                    f"{word or 'that word'} in the current Akan knowledge base."
                )
            )

        elif request_type == "related":
            answer = (
                ", ".join(related)
                if related
                else (
                    f"No explicit related words are available for "
                    f"{word or 'that term'} in the current Akan knowledge base."
                )
            )

        elif request_type == "example":
            answer = (
                " ".join(examples)
                if examples
                else (
                    f"No example sentence is currently available for "
                    f"{word or 'that word'}."
                )
            )

        elif request_type == "meaning":
            if meaning:
                answer = str(meaning)
            elif english:
                answer = str(english)
            else:
                answer = str(word or "")

        else:
            parts = []

            if word:
                parts.append(str(word))

            if english:
                parts.append(f"English: {english}")

            if meaning:
                parts.append(f"Meaning: {meaning}")

            if examples:
                parts.append(
                    f"Example: {examples[0]}"
                )

            answer = "\n".join(parts)

        confidence = min(
            0.99,
            max(
                0.20,
                score / 180.0,
            ),
        )

        return {
            "answer": answer,
            "word": word,
            "english": english,
            "meaning": meaning,
            "examples": examples,
            "synonyms": synonyms,
            "antonyms": antonyms,
            "related_words": related,
            "request_type": request_type,
            "confidence": round(confidence, 3),
            "score": score,
            "source": "akan_knowledge_base",
            "engine_version": self.VERSION,
            "record": record,
        }

    # ------------------------------------------------------------------
    # Main query interface
    # ------------------------------------------------------------------

    def answer(self, query: str) -> Dict[str, Any]:
        """Answer an Akan query."""

        if not query or not str(query).strip():
            return {
                "answer": "",
                "request_type": "general",
                "confidence": 0.0,
                "source": "akan_knowledge_base",
                "engine_version": self.VERSION,
            }

        request_type = self.detect_request_type(query)

        # --------------------------------------------------------------
        # Translation
        # --------------------------------------------------------------

        if request_type == "translation":
            target = self.extract_translation_target(query)

            if target:
                matches = self._exact_matches(target)

                if matches:
                    record, score = matches[0]

                    return self._record_response(
                        record,
                        request_type,
                        score + 30,
                    )

        # --------------------------------------------------------------
        # Meaning / synonym / antonym / related / examples
        # --------------------------------------------------------------

        target = self.extract_target_word(query)

        if target:
            matches = self._exact_matches(target)

            if matches:
                ranked = self._rank_records(
                    query,
                    matches,
                )

                record, score = ranked[0]

                return self._record_response(
                    record,
                    request_type,
                    score,
                )

        # --------------------------------------------------------------
        # General exact matching
        # --------------------------------------------------------------

        exact = self._exact_matches(query)

        if exact:
            ranked = self._rank_records(
                query,
                exact,
            )

            record, score = ranked[0]

            return self._record_response(
                record,
                request_type,
                score,
            )

        # --------------------------------------------------------------
        # General lexical fallback
        # --------------------------------------------------------------

        ranked = self._rank_records(query)

        if ranked:
            record, score = ranked[0]

            # Don't return extremely weak matches as if they were certain.
            if score >= 8:
                return self._record_response(
                    record,
                    request_type,
                    score,
                )

        # --------------------------------------------------------------
        # No answer
        # --------------------------------------------------------------

        return {
            "answer": (
                "I could not find a sufficiently relevant answer "
                "in the Akan knowledge base."
            ),
            "request_type": request_type,
            "confidence": 0.0,
            "source": "akan_knowledge_base",
            "engine_version": self.VERSION,
            "matched": False,
        }

    # ------------------------------------------------------------------
    # Compatibility aliases
    # ------------------------------------------------------------------

    def get_answer(self, query: str) -> Dict[str, Any]:
        """Compatibility alias used by other project components."""

        return self.answer(query)

    def query(self, query: str) -> Dict[str, Any]:
        """Compatibility alias."""

        return self.answer(query)

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Return ranked records for inspection/testing."""

        ranked = self._rank_records(query)

        return [
            {
                "record": record,
                "score": score,
            }
            for record, score in ranked[:10]
        ]


# ----------------------------------------------------------------------
# Module-level compatibility
# ----------------------------------------------------------------------

_default_engine: Optional[AkanEngine] = None


def get_engine() -> AkanEngine:
    """Return a lazily initialized Akan engine."""

    global _default_engine

    if _default_engine is None:
        _default_engine = AkanEngine()

    return _default_engine


def get_answer(query: str) -> Dict[str, Any]:
    """Module-level compatibility helper."""

    return get_engine().answer(query)


__all__ = [
    "AkanEngine",
    "get_engine",
    "get_answer",
]
