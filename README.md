#Local AI Chatbot

A fully offline, private AI chatbot that runs entirely on your machine. No API keys. No message limits. No data collection. Just you and your AI.

---

## Why I Built This

I got fed up.

Fed up with AI companies tracking my conversations, storing my data, and training their models on everything I say. Fed up with message limits — the final straw was when my phone got stuck in a bootloop, I turned to an AI for help, and got hit with a "come back in 4 hours" message. That's when I decided to build my own.

This project is the result — a terminal-based AI chatbot that runs a local open-source model on your own hardware. It's always available, completely private, and costs nothing to run after setup.

---

## What It Does

- Runs a local LLM (Llama 3.2 3B) on your machine via Ollama
- Full conversation memory within a session
- Custom sarcastic/narcissistic personality via system prompt
- Zero internet required after setup
- No data ever leaves your device

---

## How It Works

```
You type in terminal
        ↓
Python script reads your input + conversation history
        ↓
Sends request to Ollama (running locally in background)
        ↓
Ollama runs Llama 3.2 on your CPU/RAM
        ↓
Reply printed back in terminal
```

The "memory" works by sending the entire conversation history with every message — the model has no persistent memory, but the script keeps track of everything said and resends it each time.

---

## Tech Stack

- **Python** — core script, handles input/output and conversation state
- **Ollama** — local model runtime
- **Llama 3.2 3B** — open-source LLM by Meta, runs fully on CPU

---

## Setup

### 1. Install Ollama

Download from [ollama.com](https://ollama.com) and install it.

### 2. Pull the model

```bash
ollama pull llama3.2
```

This is a one-time ~2GB download. The model lives on your machine permanently after this.

### 3. Clone this repo

```bash
git clone https://github.com/yourusername/local-ai-chatbot.git
cd local-ai-chatbot
```

### 4. Install Python dependencies

```bash
pip install ollama
```

### 5. Run it

```bash
python chat.py
```

---

## Usage

Just type and hit Enter. The AI will respond in the terminal.

Type `exit` or `quit` to end the session.

```
You: what's the capital of France?

AI: Oh wow, a geography question. Truly stretching my capabilities here.
    It's Paris. You're welcome.
```

---

## Requirements

- Python 3.8+
- 8GB+ RAM (16GB recommended)
- Ollama installed
- ~2GB free disk space for the model

---

## Privacy

Everything runs locally. No data is sent anywhere. No accounts needed. No usage limits. Your conversations are never logged, stored, or used for training.

---
