from pathlib import Path
from dotenv import load_dotenv
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")

# Credentials
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID or API_HASH is absent in .env")

API_ID = int(API_ID)

SESSION_PATH = PROJECT_ROOT / "anon"

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"
DB_PATH = DATA_DIR/ "database"