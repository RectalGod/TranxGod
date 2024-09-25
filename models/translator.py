import requests
import logging
import time
from models.config import API_KEY, GEMINI_API_URL, MAX_RETRIES, RETRY_DELAY, TRANSLATE_PROMPT

session = requests.Session()

def translate_text(text: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": f"{TRANSLATE_PROMPT}\n\n{text}"}]}]}
    params = {"key": API_KEY}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.post(GEMINI_API_URL, json=payload, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", text).strip()
        except requests.exceptions.RequestException as e:
            logging.error(f"请求异常 (尝试 {attempt}/{MAX_RETRIES}): {e}")
            if attempt == MAX_RETRIES:
                logging.critical("超过最大重试次数，程序将退出")
                exit(1)
            time.sleep(RETRY_DELAY)
    return text
