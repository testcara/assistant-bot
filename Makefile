# Makefile for assistent_bot project

.PHONY: help install run-cli run-server run-ngrok lint format

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Available targets:"
	@echo "  install       Install Python dependencies from requirements.txt"
	@echo "  run-cli       Run the interactive CLI assistant (local or model mode)"
	@echo "  run-server    Start the Flask Slack bot server (MODE=slack)"
	@echo "  run-ngrok     Start ngrok tunnel on port 3000"
	@echo "  lint          Run black in check mode"
	@echo "  format        Format Python code with black"

install:
	pip install -r requirements.txt

run-cli:
	MODE=cli python3.11 main.py

run-server:
	MODE=slack python3 main.py


run-ngrok:
	ngrok http 3000


lint:
	black --check .

format:
	black .

