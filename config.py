import os
from typing import NamedTuple

from dotenv import load_dotenv

from utils import FileSystem, logger

dotenv_path: str = FileSystem.get_absolute_path('.env')
if os.path.exists(dotenv_path):
    logger.info(f'Load env vars from {dotenv_path}')
    load_dotenv(dotenv_path)


class Config(NamedTuple):
    base_url: str = os.environ.get("BASE_URL", "http://localhost:8080")
