# Coding Assistant – Beginner Setup Guide

This guide explains how to start and run this application even if you have never worked with AI or LLM (Large Language Model) engineering before.

The app supports:

* OpenAI models through the OpenAI Platform
* Local AI models using Ollama
* The local model currently configured is `llama3.2`

---

# What This App Does

This application connects to AI language models so users can chat with or use AI features inside the app.

The app can use:

1. **OpenAI** → cloud-based AI models accessed through an API key
2. **Ollama** → locally running AI models on your own computer

The current local model is:

```bash
llama3.2
```

---

# Before You Start

You need the following installed on your computer:

## Required Software

### 1. Git

Git is used to download the project.

Download:

https://git-scm.com

Verify installation in the terminal:

```bash
git --version
```

---

### 2. Ollama

Ollama lets you run AI models locally on your machine.

Download:

https://ollama.com

Verify installation in the terminal:

```bash
ollama --version
```

---

### 3. Python

Python allows you to run the software on your terminal or code editor.

#### macOS

Download:

Install brew from https://brew.sh/ copy the link under install homebrew and paste it into your terminal.

Install Python by running:

```bash
brew install python
```

Verify the installation with: 

```bash
python3 --version
```

#### Linux (Ubuntu/Debian)

Update your package list: 

```bash
sudo apt update
```

Install Python: 

```bash
sudo apt install python3
```

# Step 1 – Download the Project

Open a terminal or command prompt.

Run:

```bash
git clone https://github.com/Aggio98/llm_coder_bot.git
```

Then move into the project folder:

```bash
cd llm_coder_bot
```

---

# Step 2 – Install Project Dependencies

Start a virtual environment:

```bash
python3 -m venv .venv
```

Install the required dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

This downloads all required packages

---

# Step 3 – Set Up OpenAI

The app supports OpenAI models using an API key.

## Create an OpenAI Account

Go to:

https://platform.openai.com

Create an account if needed and add money to your account, add at least 5 dollar

---

## Create an API Key

Open:

https://platform.openai.com/api-keys

Create a new API key.

Copy the key.

It will look similar to:

```bash
sk-xxxxxxxxxxxxxxxx
```

---

## Add the API Key to the App

Create a file named:

```bash
.env
```

Inside the file add:

```env
OPENAI_API_KEY=openai_api_key_here
LLAMA_API_KEY=ollama
```

Replace:

```bash
openai_api_key_here
```

with your actual key.

---

# Step 4 – Set Up Ollama

The app also supports local AI using Ollama.

## Download the llama3.2 Model

Run:

```bash
ollama pull llama3.2
```

This downloads the local AI model.

---

## Start Ollama

In a terminal run:

```bash
ollama serve
```

Keep this terminal open.

---

# Step 5 – Configure the App

If the project uses environment variables, your `.env` file may look like this:

```env
OPENAI_API_KEY=your_openai_api_key_here
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

Depending on the project, there may be additional variables.

---

# Step 6 – Start the App

Run:

```bash
python3 main.py
```

---

# How the AI Setup Works

When you start the terminal app you will given the choice to choose either OpenAI or Ollama

## OpenAI Mode

When using OpenAI:

* Requests are sent to OpenAI servers
* Internet connection is required
* API usage may cost money

---

## Ollama Mode

When using Ollama:

* The AI model runs on your computer
* No internet required after download
* Usually slower than cloud AI
* More private because data stays local

Current local model:

```bash
llama3.2
```

---

# Common Commands

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start the app

```bash
python3 main.py
```

## Start Ollama

```bash
ollama serve
```

## Download the AI model

```bash
ollama pull llama3.2
```

---

# Troubleshooting

## Error: OPENAI_API_KEY missing

Make sure:

* The `.env` file exists
* The API key is correct
* The app was restarted after editing `.env`

---

## Error: Could not connect to Ollama

Make sure Ollama is running in another termianl tab:

```bash
ollama serve
```

---

## Error: llama3.2 model not found

Run:

```bash
ollama pull llama3.2
```

---

# Recommended Computer Specs

For local AI models:

Minimum:

* 8GB RAM
* Modern CPU

Recommended:

* 16GB+ RAM
* Dedicated GPU

---

# Project Structure Example

```bash
project/
│
├── .venv/            # Virutal environemnt
├── .env              # Application source code
├── config.py         # Static files
├── main.py           # Environment variables
├── README.md         # Project dependencies
└── requirements.txt  # This file
```

---

# Useful Links

* urlOpenAI Platform[https://platform.openai.com](https://platform.openai.com)
* urlOpenAI Documentation[https://platform.openai.com/docs](https://platform.openai.com/docs)
* urlOllama Documentation[https://ollama.com/library](https://ollama.com/library)

---

# Final Notes

If the app does not start:

1. Make sure python is installed and you created a virtual environment
2. Make sure dependencies were installed using `pip install -r requirements.txt`
3. Make sure the `.env` file exists
4. Make sure Ollama is running
5. Make sure the `llama3.2` model has been downloaded

Once everything is running, the application should connect to either OpenAI or the local Ollama model automatically depending on the configuration.
