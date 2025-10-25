# ==== General ====
DEBUG = True
MAX_ARTICLES = 10  # how many latest news to fetch each run
LOG_FILE = "logs/run.log"

RECENT_MERGED_PATH = "output/news/merged_latest_recent.json"
LOG_FILE = "logs/scrape_log.txt"

# ==== News Fetcher (Moneycontrol) ====
MONEYCONTROL_RAW_NEWS_PATH = "output/news/moneycontrol/moneycontrol_latest.json"              # cumulative raw articles
MONEYCONTROL_RECENT_NEWS_PATH = "output/news/moneycontrol/moneycontrol_latest_recent.json"    # recent batch (overwrites each run)

LIVEMINT_RAW_NEWS_PATH   = "output/news/livemint/livemint_latest.json"
LIVEMINT_RECENT_NEWS_PATH = "output/news/livemint/livemint_latest_recent.json"

CNBC_RAW_NEWS_PATH   = "output/news/cnbc_tv18/cnbc_latest.json"
CNBC_RECENT_NEWS_PATH = "output/news/cnbc_tv18/cnbc_latest_recent.json"


ET_RAW_NEWS_PATH    = "output/news/the_economic_times/et_latest.json"
ET_RECENT_NEWS_PATH = "output/news/the_economic_times/et_latest_recent.json"

# ==== Company Tagger ====
MAPPING_CSV_PATH = "data/Nifty50BankNifty_mapping.csv"
TAGGED_OUTPUT_PATH = "output/processed_articles/tagged_articles.json"
TAGGED_RECENT_PATH = "output/processed_articles/tagged_articles_recent.json"

# ==== Sentiment Model (Positive / Neutral / Negative) ====
LABELED_OUTPUT_PATH = "output/labeled_articles/labeled_articles.json"
LABELED_RECENT_PATH = "output/labeled_articles/labeled_articles_recent.json"

# Tunables (safe to tweak)
SENT_BATCH_SIZE = 8
SENT_CHUNK_CHARS = 1800      # ~rough proxy for 512 tokens
SENT_MAX_CHUNKS = 6
SENT_NEUTRAL_MARGIN = 0.06   # if (top - second) < margin => Neutral
SENT_MIN_TOP_CONF = 0.55     # if top prob < this => Neutral
SENT_MIN_CONTENT_CHARS = 200 # if content shorter => Neutral

# ==== Aggregation ====
AGGREGATED_OUTPUT_PATH = "output/aggregated_sentiment/aggregated.json"
AGGREGATED_RECENT_PATH = "output/aggregated_sentiment/aggregated_recent.json"

# ==== Volatility Filter ====
FILTERED_OUTPUT_PATH = "output/filtered_signals/filtered.json"
FILTERED_RECENT_PATH = "output/filtered_signals/filtered_recent.json"

# method: "stdev" (std dev of daily % change) or "atr" (ATR% of close)
MIN_VOLATILITY = 1.2          # % threshold to keep an entity
VOL_METHOD = "stdev"
VOL_LOOKBACK_DAYS = 20
VOL_MIN_DATA_POINTS = 12

# yfinance overrides (add here if any symbol doesn’t map to *.NS cleanly)
YF_SYMBOL_OVERRIDES = {
    # "AIRTEL": "BHARTIARTL.NS",
}

# Index shortcuts (used in volatility + signals)
INDEX_SYMBOLS = {
    "NIFTY": "^NSEI",
    "NIFTY 50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "BANK NIFTY": "^NSEBANK",
}


# ==== Trade Signals ====
SIGNALS_OUTPUT_PATH = "output/signals/signals.json"
SIGNALS_RECENT_PATH = "output/signals/signals_recent.json"

# thresholds 
STOCK_THRESHOLD = 90   # % for stocks
INDEX_THRESHOLD = 70   # % for indices (Nifty, BankNifty)

SIGNALS_OUTPUT_PATH = "output/signals/signals.json"
SIGNALS_RECENT_PATH = "output/signals/signals_recent.json"
STOCK_THRESHOLD = 90
INDEX_THRESHOLD = 70
INDEX_SYMBOLS = { 
    "NIFTY": "^NSEI",
    "NIFTY 50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "BANK NIFTY": "^NSEBANK",
}

