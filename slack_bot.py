# slack_bot.py
import os
import logging
import requests
from flask import Blueprint, request, jsonify
from retriever import generate_answer

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

slack_blueprint = Blueprint("slack_bot", __name__)
current_mode = os.getenv("DEFAULT_ANSWER_MODE", "local")  # 默认模式

def reply_to_slack(channel, text):
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"channel": channel, "text": text}
    r = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)
    if not r.ok:
        logging.error(f"Slack error: {r.text}")

@slack_blueprint.route("/slack/events", methods=["POST"])
def slack_events():
    global current_mode
    data = request.json

    if data.get("type") == "url_verification":
        return jsonify({"challenge": data["challenge"]})

    if data.get("type") == "event_callback":
        event = data.get("event", {})
        if event.get("type") == "app_mention":
            raw_text = event.get("text", "")
            channel = event.get("channel")

            # Remove bot mention
            user_question = ' '.join(raw_text.split()[1:]).strip()
            logging.info(f"Slack question: {user_question}")

            # Handle mode switching
            if user_question.lower().startswith("!mode"):
                parts = user_question.split()
                if len(parts) == 2 and parts[1] in ["local", "model", "auto"]:
                    current_mode = parts[1]
                    reply_to_slack(channel, f"Answer mode switched to *{current_mode}*.")
                else:
                    reply_to_slack(channel, "Usage: `!mode local|model|auto`")

    return "OK", 200
