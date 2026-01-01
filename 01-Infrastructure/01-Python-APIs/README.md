# 🔌 Module 01: Python APIs & Infrastructure

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Focus](https://img.shields.io/badge/Focus-JSON%20%26%20Error%20Handling-purple)

This module forms the foundation of the agentic roadmap. It focuses on robustly connecting to **OpenAI** and **Anthropic** models, enforcing structured **JSON outputs**, and handling production-grade errors like rate limits.

---

## 🧠 Module Goal
**To treat LLMs as functional APIs, not chat bots.**
Reliable agents require reliable inputs and outputs. This module builds the wrapper clients that ensure our agents speak "Code" (JSON), not "English".

## 📂 Repository Structure

```text
01-Python-APIs/
├── openai_client/       # OpenAI specific implementations
│   └── openai_json.py   # GPT-4o Wrapper with Retry Logic
├── anthropic_client/    # Anthropic specific implementations
│   └── claude_json.py   # Claude 3.5 Sonnet Wrapper
├── cli_tools/           # Command-line tools
│   └── summarize.py     # CLI Text Summarizer
└── utils/               # Shared Utilities
    └── json_utils.py    # Safe JSON Parsing & Validation
```
## 🛠️ Key Concepts Implemented

* **Structured Outputs:** Forcing models to return valid JSON schemas (e.g., extracting `Task`, `Difficulty`, `Tools`) using system prompts.
* **Resilience Patterns:** Implementing **Exponential Backoff** to handle `RateLimitError` without crashing.
* **Safety Layers:** A centralized `json_utils` parser to sanitize LLM responses before they hit your application logic.
* **CLI Engineering:** Building modular command-line interfaces using `argparse`.

---

## 💻 How to Run

**Prerequisites:**
1. Navigate to this folder: `cd 01-Python-APIs`
2. Install SDKs: `pip install openai anthropic`
3. Ensure `.env` keys are set in the parent directory.

### 1. OpenAI JSON Generator
*Runs the GPT wrapper with automatic retries.*
```bash
python -m openai_client.openai_json
```

### 2. Anthropic (Claude) JSON Generator
*Runs the Claude wrapper with strict type enforcement.*
```bash
python -m anthropic_client.claude_json
```

### Usage: python cli_tools/summarize.py
```bash
python cli_tools/summarize.py sample_data.txt
```
