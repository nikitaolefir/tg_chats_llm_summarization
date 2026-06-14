import sqlite3
from tg_digest.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
            chat_id    INTEGER,
            message_id INTEGER,
            date       INTEGER,
            sender_id  INTEGER,
            text       TEXT,
            reply_to   INTEGER,
            PRIMARY KEY (chat_id, message_id)
            )""")
    conn.commit()
    conn.close()


def insert_messages(messages):
    conn = get_connection()
    conn.executemany(
        """INSERT OR REPLACE INTO messages
               (chat_id, message_id, date, sender_id, text, reply_to)
           VALUES (:chat_id, :message_id, :date, :sender_id, :text, :reply_to)""",
        messages,
    )
    conn.commit()
    conn.close()


def read_messages(chat_id=None, start=None, end=None):
    conn = get_connection()
    query = "SELECT * FROM messages"
    conditions = []
    params = []

    if chat_id is not None:
        conditions.append("chat_id = ?")
        params.append(chat_id)
    if start is not None:
        conditions.append("date >= ?")
        params.append(start)
    if end is not None:
        conditions.append("date <= ?")
        params.append(end)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY date"

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows
