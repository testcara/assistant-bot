from flask import Flask
from dotenv import load_dotenv
import os
from logger import setup_logger
from slack_bot import slack_blueprint

load_dotenv()
setup_logger()

app = Flask(__name__)
app.register_blueprint(slack_blueprint)

if __name__ == "__main__":
    app.run(port=3000)
