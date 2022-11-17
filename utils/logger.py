import datetime
import os.path

from utils import FileSystem
from loguru import logger


logs_folder_path: str = FileSystem.get_absolute_path("logs")
log_name: str = f'{datetime.datetime.now().strftime("%d-%m_%H_%M")}.log'
logger.add(os.path.join(logs_folder_path, log_name), rotation="500 MB")
