# 🤖 assistent_bot

A local AI assistant that supports Slack bot integration and command-line Q&A. It leverages a simple local RAG (Retrieval-Augmented Generation) pipeline using your own `.md` or `.txt` documents and can fall back to large models via Ollama when needed.

---

## 🧩 Features

- 🔎 Document-based RAG question answering
- 💬 Command-line interface (CLI) mode
- 🤖 Slack bot integration with slash mention and `!mode` switching
- 🧠 Choose between:
  - `local` (use local documents)
  - `model` (use local specific model served by Ollama without document context)

---

## 🗂️ Project Structure

```bash
.
├── Makefile
├── Readme.md
├── app.py
├── cli.py
├── logger.py
├── main.py
├── my_docs
│   ├── about_CUE.txt
│   ├── about_banner.txt
│   ├── about_cara.txt
│   └── about_ui.txt
├── ollama.py
├── requirements.txt
├── retriever.py
└── slack_bot.py
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourname/assistent_bot.git
cd assistent_bot
```

### 2. Install dependencies

```bash
make install
```

### 3. Prepare your .env file

Create a .env file in the root folder:

```bash
SLACK_BOT_TOKEN=your-slack-bot-token
MODE=cli          # or slack
DEFAULT_ANSWER_MODE=local # or model
```

## 🧠 Usage

### 💬 CLI Mode

```bash
make run-cli
```

Example:

```bash
Your question: what is konflux banner?
Answer: Konflux banner project is aimed to support users...
```

### 🤖 Slack Bot Mode(Experimental)

1. Start the server:

```bash
make run-server
```

2. (Optional) Use ngrok to expose your server:

```bash
make run-ngrok
```

Set your Slack App's event URL to https://<your-ngrok-id>.ngrok.io/slack/events

In Slack, mention the bot:

```bash
@your-bot what's the konflux banner?
```

Switch answer mode inside Slack:

```bash
    @your-bot !mode local
    @your-bot !mode model
```

## 🛠️ Makefile Commands

### Command	Description

```bash
make install	Install all Python dependencies
make run-cli	Launch interactive CLI mode
make run-server	Start Flask server for Slack bot
make run-ngrok	Start ngrok tunnel for testing Slack
make lint	Run black formatting check
make format	Format code using black
```

## 📄 Customize Your Knowledge Base

Put your .md or .txt files into the my_docs/ folder.

```bash
my_docs/
├── konflux-banner.md
├── cara-team-notes.md
```

These documents will be used for local retrieval when DEFAULT_ANSWER_MODE=local.