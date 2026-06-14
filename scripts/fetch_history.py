from datetime import datetime, timezone, timedelta
from tg_digest.config import load_chats
from tg_digest.tg_client import get_client
from tg_digest.storage import init_db, insert_messages
from tg_digest.extract import fetch_messages
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logging.getLogger("telethon").setLevel(logging.WARNING)
log = logging.getLogger(__name__)


def main():
    init_db()
    chats = load_chats()
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=7)
    with get_client() as client:
        for chat in chats:
            log.info("Downloading: %s", chat["name"])
            messages = fetch_messages(client, chat["id"], start, end)
            insert_messages(messages)
            log.info("%s: %d messages collected", chat["name"], len(messages))

if __name__ == "__main__":
    main()
