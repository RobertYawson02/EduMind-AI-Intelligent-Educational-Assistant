"""Durable, session-isolated conversation storage.

SQLite is used by default for local development. Set DATABASE_URL to a
PostgreSQL URL in hosted deployments so multiple workers can share state.
"""

import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Any, Dict, List


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SQLITE_PATH = os.path.join(BASE_DIR, "data", "conversations.sqlite3")


def _database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///" + DEFAULT_SQLITE_PATH)


def _is_postgres() -> bool:
    return _database_url().startswith(("postgres://", "postgresql://"))


@contextmanager
def _connection():
    url = _database_url()
    if _is_postgres():
        try:
            import psycopg
        except ImportError as exc:
            raise RuntimeError("DATABASE_URL requires the psycopg package") from exc
        connection = psycopg.connect(url)
        try:
            yield connection
            connection.commit()
        finally:
            connection.close()
        return

    path = url.removeprefix("sqlite:///")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    connection = sqlite3.connect(path, timeout=30)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_store() -> None:
    with _connection() as connection:
        cursor = connection.cursor()
        if _is_postgres():
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS conversation_turns (
                    id BIGSERIAL PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    intent TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    language TEXT NOT NULL,
                    confidence DOUBLE PRECISION NOT NULL,
                    sources JSONB NOT NULL
                )
                """
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS conversation_turns_session_idx "
                "ON conversation_turns (session_id, id)"
            )
        else:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS conversation_turns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    intent TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    language TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    sources TEXT NOT NULL
                )
                """
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS conversation_turns_session_idx "
                "ON conversation_turns (session_id, id)"
            )


def load_turns(session_id: str, limit: int = 20) -> List[Dict[str, Any]]:
    initialize_store()
    with _connection() as connection:
        cursor = connection.cursor()
        placeholder = "%s" if _is_postgres() else "?"
        cursor.execute(
            "SELECT created_at, question, answer, intent, topic, language, "
            f"confidence, sources FROM conversation_turns WHERE session_id = {placeholder} "
            "ORDER BY id DESC LIMIT " + str(max(1, int(limit))),
            (session_id,),
        )
        rows = cursor.fetchall()

    turns = []
    for row in reversed(rows):
        values = dict(row) if hasattr(row, "keys") else dict(zip(
            ["timestamp", "question", "answer", "intent", "topic", "language", "confidence", "sources"], row
        ))
        values["timestamp"] = values.pop("created_at", values.get("timestamp"))
        sources = values.get("sources", [])
        values["sources"] = sources if isinstance(sources, list) else json.loads(sources or "[]")
        turns.append(values)
    return turns


def save_turn(session_id: str, turn: Dict[str, Any]) -> None:
    initialize_store()
    with _connection() as connection:
        cursor = connection.cursor()
        placeholder = "%s" if _is_postgres() else "?"
        sources = turn.get("sources", [])
        if _is_postgres():
            sources = json.dumps(sources)
        else:
            sources = json.dumps(sources, ensure_ascii=False)
        cursor.execute(
            "INSERT INTO conversation_turns "
            "(session_id, created_at, question, answer, intent, topic, language, confidence, sources) "
            f"VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})",
            (
                session_id,
                turn.get("timestamp", datetime.now(timezone.utc).isoformat()),
                turn.get("question", ""),
                turn.get("answer", ""),
                turn.get("intent", "general"),
                turn.get("topic", "general"),
                turn.get("language", "english"),
                float(turn.get("confidence", 0.0)),
                sources,
            ),
        )


def clear_turns(session_id: str) -> None:
    initialize_store()
    with _connection() as connection:
        cursor = connection.cursor()
        placeholder = "%s" if _is_postgres() else "?"
        cursor.execute(f"DELETE FROM conversation_turns WHERE session_id = {placeholder}", (session_id,))