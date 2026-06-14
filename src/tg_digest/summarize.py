"""Тематическая суммаризация переписки через локальную LLM (Ollama)."""
import json
import logging

import ollama

from tg_digest import config

log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "Ты ассистент, который читает переписку из группового чата и делает "
    "тематический дайджест. В чате темы идут вперемешку — выдели отдельные "
    "темы обсуждения. Для каждой темы дай короткий заголовок и саммари из "
    "1–3 предложений на русском языке. Верни результат строго в JSON по "
    "заданной схеме, без какого-либо текста вне JSON."
)

SUMMARY_SCHEMA = {
    "type": "object",
    "properties": {
        "topics": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "summary": {"type": "string"},
                },
                "required": ["title", "summary"],
            },
        }
    },
    "required": ["topics"],
}


def summarize(text, model=config.OLLAMA_MODEL):
    """Сделать тематический дайджест переписки.

    На вход — склеенный текст сообщений за период.
    Возвращает dict вида {"topics": [{"title": ..., "summary": ...}, ...]}
    или None, если модель вернула невалидный JSON.
    """
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        format=SUMMARY_SCHEMA,
        options={"num_ctx": config.OLLAMA_NUM_CTX, "temperature": 0.2},
    )
    content = response["message"]["content"]
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        log.error("Модель вернула невалидный JSON: %s", content[:500])
        return None
