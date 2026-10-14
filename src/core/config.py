import os
from pathlib import Path

from dotenv import dotenv_values


_ENV_FILE = Path(__file__).with_name(".env")
_FILE_SETTINGS = dotenv_values(_ENV_FILE)


def _setting(name: str, default: str) -> str:
    return os.environ.get(name) or _FILE_SETTINGS.get(name) or default


OLLAMA_API_URL = _setting(
    "OLLAMA_API_URL",
    "http://localhost:11434/api/chat",
)
OLLAMA_MODEL = _setting("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_API_KEY = (
    os.environ.get("OLLAMA_API_KEY")
    or _FILE_SETTINGS.get("OLLAMA_API_KEY")
    or None
)