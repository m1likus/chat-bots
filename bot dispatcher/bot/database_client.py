import sqlite3
import os
import json
from dotenv import load_dotenv

load_dotenv()


def persist_updates(updates: dict) -> None:
    payload = json.dumps(updates, ensure_ascii=False, indent=2)
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            connection.execute(
                "INSERT INTO telegram_updates (payload) VALUES (?)", (payload,)
            )


def recreate_database() -> None:
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        with connection:
            connection.execute("DROP TABLE IF EXISTS telegram_updates")
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS telegram_updates
                (
                    id INTEGER PRIMARY KEY,
                    payload TEXT NOT NULL
                )
                """,
            )
