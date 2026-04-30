import logging
import logging
import os
from datetime import datetime

LOG_DIR="logs"
LOG_FILE=os.path.join(LOG_DIR,"automoto.log")
ERROR_FILE=os.path.join(LOG_DIR,"errors.log")
SESSION_FILE=os.path.join(LOG_DIR,"session.log")

LOG_FORMAT="%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
LOG_DATE_FORMAT="%Y-%m-%d %H:%M:%S"

os.makedirs(LOG_DIR,exist_ok=True)
logger=logging.getLogger(__name__)

def setup_logger(name: str="AutoMoto") -> logging.Logger:

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)

    # handler 1 : console output
    console_handler=logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter=logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)

    #handler 2 : Main log file

    file_handler=logging.FileHandler(LOG_FILE,encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_formatter=logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )

    file_handler.setFormatter(file_formatter)

    #Handler 3 : Error-only log file

    error_handler=logging.FileHandler(ERROR_FILE,encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)

    return logger

def log_session_start() -> str:
    os.makedirs(LOG_DIR,exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    separator = "=" * 60

    with open(SESSION_FILE,"a",encoding="utf-8") as f:
        f.write(f"\n {separator}\n")
    
def log_session_end()-> None:
    os.makedirs(LOG_DIR,exist_ok=True)
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")   

    with open(SESSION_FILE,"a", encoding="utf-8") as f:
        f.write(f"Session Ended : {timestamp} \n")
        f.write(f"{'='*60}\n")

def log_command(command: str, response: str) -> None:
    os.makedirs(LOG_DIR,exist_ok=True)
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    with open(SESSION_FILE,"a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] CMD : {command}\n")
        f.write(f"[{timestamp}] RESP: {response[:100]}\n")
        f.write(f" {'-' *50}\n")