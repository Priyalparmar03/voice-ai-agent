import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

def log_event(msg):
    logging.info(msg)