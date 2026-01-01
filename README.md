# 🚀 AI Agentic Engineering Roadmap

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Focus](https://img.shields.io/badge/Focus-AI%20Agents%20%26%20RAG-green)

A comprehensive engineering roadmap to master **AI Agents**, **RAG (Retrieval Augmented Generation)**, and **Multi-Agent Systems**. 

This repository documents the journey from writing basic LLM scripts to building production-grade autonomous agent systems that can plan, reason, and execute tasks.

---

## 🧠 Project Goal
**To move beyond "Chatbots" and build "Agents".** While chatbots just talk, **Agents** use tools, search the web, write code, and execute complex workflows. This repository serves as a portfolio of structured learning and building.

## 📂 Repository Structure

The project is organized into 4 high-level modules, progressing from infrastructure to deployment.

### 🔹 Module 01: Infrastructure & RAG
*Focus: Tying LLMs to data and memory.*
- [x] **01_Python_APIs**: Handling OpenAI/Anthropic API calls and structured JSON outputs.
- [x] **02_Vector_DBs**: Implementing semantic search (Pinecone/ChromaDB).
- [ ] **03_Basic_RAG**: Building "Chat with PDF" using LangChain.
- [ ] **04_Advanced_RAG**: Hybrid search, Re-ranking, and hallucination reduction.

### 🔹 Module 02: Single Agent Architectures
*Focus: Teaching AI to use tools and reason.*
- [ ] **01_Tool_Use**: Function calling (Connecting LLMs to Calculators/APIs).
- [ ] **02_ReAct_Pattern**: Implementing the "Reason + Act" loop.
- [ ] **03_Structured_Output**: Enforcing strict JSON schemas with Pydantic.
- [ ] **04_Agentic_Memory**: Managing long-term state with LangGraph.

### 🔹 Module 03: Multi-Agent Systems
*Focus: Orchestrating a team of AI employees.*
- [ ] **01_Agent_Patterns**: Building "Software House" simulations (Coder + Reviewer).
- [ ] **02_Routing_Planning**: Hierarchical task management & Supervisors.
- [ ] **03_Human_in_Loop**: Approval workflows for critical actions.
- [ ] **04_Evaluation_Ops**: Automated testing and evaluation datasets.

### 🔹 Module 04: Production & Deployment
*Focus: The Flagship Portfolio Project.*
- [ ] **01_FastAPI_Backend**: Wrapping agents in robust REST APIs.
- [ ] **02_Frontend_UI**: Building interfaces with Streamlit/Vercel.
- [ ] **03_The_Autonomous_Analyst**: 🚩 **Flagship Project** (Data Analysis + Charting + Reporting).

---

## 🛠️ Tech Stack

* **Languages:** Python
* **LLMs:** OpenAI (GPT-4), Anthropic (Claude 3.5)
* **Orchestration:** LangChain, LangGraph
* **Vector DBs:** Pinecone, ChromaDB
* **Serving:** FastAPI, Streamlit

---

## 💻 How to Run This Code

Each module in this repository is self-contained. To run the code, please follow the specific instructions inside each module folder.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AI-Agentic-Engineering-Roadmap.git](https://github.com/YOUR_USERNAME/AI-Agentic-Engineering-Roadmap.git)
    cd AI-Agentic-Engineering-Roadmap
    ```

2.  **Set up Environment Variables:**
    Create a `.env` file in your project root and add your API keys:
    ```env
    OPENAI_API_KEY="sk-..."
    ANTHROPIC_API_KEY="sk-..."
    ```

3.  **Install Dependencies:**
    Navigate to the specific module you are working on (e.g., `01_Infrastructure/01_Python_APIs`) and install the requirements listed there.

---

## 📈 Roadmap Phases
* **Phase 1:** Infrastructure (Current)
* **Phase 2:** Single Agents
* **Phase 3:** Multi-Agent Orchestration
* **Phase 4:** Deployment & Portfolio

---

*This roadmap follows the "AI Agentic Specialist" curriculum.*
