from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
SYSTEM_PROMPT_PATH = DOCS_DIR / "03-prompts.md"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-5.4-mini"