from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB_DIR = ROOT / "data" / "knowledge"
SCHEMES_FILE = ROOT / "data" / "schemes.json"
DB_PATH = ROOT / "data" / "app.db"
CHROMA_DIR = str(ROOT / "chroma_db")

EMBED_MODEL = "BAAI/bge-m3"
LLM_MODEL = "gemma3:4b"      # try "qwen2.5:3b" later and compare
TOP_K = 4
MIN_CONFIDENCE = 0.45         # tune this in Step 7