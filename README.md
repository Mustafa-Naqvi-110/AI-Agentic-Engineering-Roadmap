🔌 Module 01: Python APIs & Foundation
The foundational layer for the AI Agentic Engineering Roadmap.

Before building complex agents, we must master the "atomic" operations: reliably connecting to LLMs (OpenAI & Anthropic), handling rate limits, and forcing models to output machine-readable data (JSON) instead of unstructured chat.

📂 Module Structure
This module is organized into provider-specific clients and shared utilities.

Plaintext

01-Python-APIs/
├── openai_client/       # OpenAI implementation
│   └── openai_json.py   # GPT-4o with retry logic
├── anthropic_client/    # Anthropic implementation
│   └── claude_json.py   # Claude 3.5 Sonnet with safe parsing
├── cli_tools/           # Command-line tools
│   └── summarize.py     # CLI text summarizer
└── utils/               # Shared Engineering Utilities
    └── json_utils.py    # Robust JSON parser/validator
🛠️ Key Engineering Patterns
1. Structured Outputs (JSON)
Agents communicate via code, not chat. This module demonstrates how to prompt effectively to receive strict JSON schemas (e.g., { "task": "...", "difficulty": 5 }) rather than conversational text.

2. Fault Tolerance (Retries)
Production APIs fail. The openai_json.py implementation includes Exponential Backoff logic to handle RateLimitError and connection timeouts gracefully without crashing the application.

3. Safe Parsing
LLMs sometimes return "dirty" JSON (e.g., wrapped in markdown backticks). The utils/json_utils.py module acts as a sanitizer to prevent runtime errors during parsing.

💻 How to Run
Prerequisites: Ensure you are in the root of the 01-Python-APIs folder and have your .env keys set.

1. Install Dependencies

Bash

pip install openai anthropic
2. Run OpenAI JSON Generator Demonstrates retry logic and schema enforcement.

Bash

python -m openai_client.openai_json
3. Run Claude JSON Generator Demonstrates Anthropic integration and safe parsing.

Bash

python -m anthropic_client.claude_json
4. Run Text Summarizer (CLI) A practical tool to summarize local text files.

Bash

# Create a dummy file first if you don't have one
echo "AI Agents are systems that use LLMs as reasoning engines to determine which actions to take and in what order." > test.txt

# Run the summarizer
python cli_tools/summarize.py test.txt
