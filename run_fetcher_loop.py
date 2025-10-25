import time
import logging
from pathlib import Path
from news_fetcher import fetch_all_sources

INTERVAL = 60
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "news_fetcher_loop.log", encoding="utf-8"),
        logging.StreamHandler()
    ],
)

try:
    while True:
        try:
            logging.info("Starting fetch run")
            fetch_all_sources()
            logging.info("Fetch run completed")
        except Exception:
            logging.exception("Fetch run failed")
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    logging.info("Stopped by user (KeyboardInterrupt)")

