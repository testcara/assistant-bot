import requests
import logging

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt: str, model: str = "qwen2.5:0.5b", max_tokens: int = 500) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        result = data.get("completion") or data.get("response", "").strip()
        logging.debug(f"Prompt: {prompt[:80]}... | Response: {result[:80]}...")
        return result
    except Exception as e:
        logging.error(f"Ollama error: {e}")
        return ""

