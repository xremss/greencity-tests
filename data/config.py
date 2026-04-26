import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    BASE_UI_URL = os.getenv("BASE_URL")
    IMPLICIT_WAIT_TIMEOUT = int(os.getenv("IMPLICIT_WAIT_TIMEOUT"))
    EXPLICIT_WAIT_TIMEOUT = int(os.getenv("EXPLICIT_WAIT_TIMEOUT"))
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    USER_NAME = os.getenv("USER_NAME")
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "True").lower() in ("true", "1", "t")
    INVALID_EMAIL = os.getenv("INVALID_EMAIL")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")