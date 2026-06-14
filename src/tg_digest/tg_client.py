from tg_digest import config
from telethon import TelegramClient

def get_client() -> TelegramClient:
    return TelegramClient(str(config.SESSION_PATH), config.API_ID, config.API_HASH)