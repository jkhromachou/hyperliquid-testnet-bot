import logging, requests

def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("hyperliquid_bot")

def send_discord_message(msg, discord_url):
    if not discord_url:
        return
    try:
        requests.post(discord_url, json={"content": msg}, timeout=5)
    except Exception:
        pass
