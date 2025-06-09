
import os
from logger import setup_logger
from dotenv import load_dotenv
load_dotenv()
setup_logger()

MODE = os.getenv("MODE", "cli")

if MODE == "cli":
    from cli import interactive_qa
    interactive_qa()
elif MODE == "server":
    from app import app
    app.run(port=3000)
