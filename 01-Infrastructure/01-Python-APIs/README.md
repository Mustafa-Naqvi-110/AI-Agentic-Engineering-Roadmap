Markdown

# 🤖 Python GenAI API Toolkit

A robust collection of Python scripts demonstrating how to integrate **OpenAI** and **Anthropic (Claude)** APIs into production-ready workflows. This repository focuses on structured JSON data extraction, command-line tooling, and fault-tolerant API communication.

## 📂 Project Structure

```text
01-Python-APIs/
├── openai_client/       # OpenAI specific implementations
│   └── openai_json.py   # Robust JSON generation with retry logic
├── anthropic_client/    # Anthropic specific implementations
│   └── claude_json.py   # Claude 3.5 Sonnet JSON generation
├── cli_tools/           # Command-line interface tools
│   └── summarize.py     # CLI tool for summarizing text files
└── utils/               # Shared utility functions
    └── json_utils.py    # Safe JSON parsing helper
✨ Key Features
CLI Summarizer: A command-line tool to ingest text files and generate concise summaries using OpenAI models.

Structured Output: Dedicated modules (openai_json.py, claude_json.py) designed to force and validate JSON schemas from LLMs.

Resilience: Implements exponential backoff strategies for handling RateLimitError and API timeouts.

Safety: Centralized utility to safely parse LLM string outputs into Python dictionaries, preventing runtime crashes on malformed JSON.

🛠️ Prerequisites
Python 3.8+

API Keys for OpenAI and Anthropic.

Installation
Clone the repository:

Bash

git clone [https://github.com/yourusername/01-Python-APIs.git](https://github.com/yourusername/01-Python-APIs.git)
cd 01-Python-APIs
Install dependencies: You will need the official SDKs.

Bash

pip install openai anthropic
🔐 Configuration
Set your API keys as environment variables to keep them secure.

Mac/Linux:

Bash

export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
Windows (Powershell):

PowerShell

$env:OPENAI_API_KEY="sk-..."
$env:ANTHROPIC_API_KEY="sk-ant-..."
🚀 Usage Guide
Note: All commands should be run from the root directory (01-Python-APIs/) to ensure imports resolve correctly.

1. Text Summarizer (CLI)
A script to summarize local text files via the command line.

Usage:

Bash

python cli_tools/summarize.py path/to/your/document.txt
Tip: Ensure the model parameter in summarize.py is set to a valid model ID (e.g., gpt-4o or gpt-3.5-turbo).

2. OpenAI JSON Generator
Generates structured data (Schema: Task, Difficulty, Tools) using OpenAI models. This script includes built-in retry logic.

Run as a module:

Bash

python -m openai_client.openai_json
3. Anthropic (Claude) JSON Generator
Generates structured data (Schema: Model, Use_Case, Confidence) using Claude 3.5 Sonnet.

Run as a module:

Bash

python -m anthropic_client.claude_json
🧩 Code Details
utils/json_utils.py
Contains the parse_json_safely function. This wrapper ensures that if an LLM returns a string that isn't valid JSON, the program raises a clean, readable ValueError instead of a cryptic decoding error.

Error Handling
Both client scripts (openai_json.py and claude_json.py) wrap API calls in a retry loop:

Python

for attempt in range(retries):
    try:
        # API Call
    except RateLimitError:
        time.sleep(2 ** attempt) # Exponential backoff
🤝 Contributing
Contributions are welcome! Please ensure any new modules follow the existing folder structure and utilize the shared utils for parsing.
