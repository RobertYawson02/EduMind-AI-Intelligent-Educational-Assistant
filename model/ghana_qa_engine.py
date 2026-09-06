"""Ghana-QA retrieval engine.

The engine is optional: the application remains fully functional when the
large Ghana-QA CSV has not yet been downloaded. When present, it uses TF-IDF
and cosine similarity and returns several strong candidates for ranking.
"""

import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from model.dataset_manager import dataset_available, load_dataset, dataset_path


class GhanaQAEngine:
    def __init__(self, min_similarity=0.25):
        self.ready = False
        self.df = None
        self.dataset_name = "ghana_qa"
        self.vectorizer = None
        self.matrix = None
        self.min_similarity = min_similarity
        self.question_column = None
        self.answer_column = None
        self.language_column = None
        self._build_index()

    def _build_index(self):
        if not dataset_available("ghana_qa"):
            return

        df = load_dataset("ghana_qa")
        if df is None or df.empty:
            return

        columns = {str(c).strip().lower(): c for c in df.columns}
        self.question_column = columns.get("question")
        self.answer_column = columns.get("answer")
        self.language_column = columns.get("lang") or columns.get("language")

        if not self.question_column or not self.answer_column:
            return

        work = df[[self.question_column, self.answer_column]].copy()
        work = work.dropna(subset=[self.question_column, self.answer_column])
        work[self.question_column] = work[self.question_column].astype(str).str.strip()
        work[self.answer_column] = work[self.answer_column].astype(str).str.strip()
        work = work[(work[self.question_column] != "") & (work[self.answer_column] != "")]
        if work.empty:
            return

        self.df = df.loc[work.index].copy()
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            sublinear_tf=True,
            max_features=250000,
        )
        self.matrix = self.vectorizer.fit_transform(
            work[self.question_column].tolist()
        )
        self.ready = True

    def search(self, question, language=None, limit=5):
        if not self.ready or not question:
            return []

        try:
            query = str(question).strip()
            scores = cosine_similarity(
                self.vectorizer.transform([query]), self.matrix
            )[0]
            order = scores.argsort()[::-1]
            results = []

            for index in order[: max(limit * 4, limit)]:
                score = float(scores[index])
                if score < self.min_similarity:
                    break

                row = self.df.iloc[index]
                if language and self.language_column:
                    row_language = str(row.get(self.language_column, "")).lower()
                    if language == "akan" and row_language not in {"twi", "akan"}:
                        continue

                results.append({
                    "question": str(row[self.question_column]),
                    "answer": str(row[self.answer_column]),
                    "score": round(score, 6),
                    "language": str(row.get(self.language_column, "")) if self.language_column else "",
                    "dataset": os.path.basename(dataset_path("ghana_qa") or ""),
                })
                if len(results) >= limit:
                    break

            return results
        except Exception as exc:
            print(f"Ghana-QA search error: {exc}")
            return []


engine = GhanaQAEngine()


def search_ghana_qa(question, language=None, limit=5):
    return engine.search(question, language=language, limit=limit)
