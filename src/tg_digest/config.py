from pathlib import Path
from dotenv import load_dotenv
import os
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")

# Credentials
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID or API_HASH is absent in .env")

API_ID = int(API_ID)

SESSION_PATH = PROJECT_ROOT / "anon"

CONFIG_PATH = PROJECT_ROOT / "config.yaml"
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"
DB_PATH = DATA_DIR / "database.db"

OLLAMA_MODEL = "llama3.1:8b-instruct-q4_K_M"
OLLAMA_NUM_CTX = 16384


def load_chats():
    if not CONFIG_PATH.exists():
        raise RuntimeError(f"No {CONFIG_PATH}. Copy config.example.yaml into config.yaml and populate with your chats")
    with open(CONFIG_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [c for c in data["chats"] if c.get("enabled", True)]

