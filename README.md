# 🎤 Multilingual Voice-Controlled AI Agent (Local + Safe AI System)

A fully local AI agent that accepts voice input, understands user intent, and safely executes tasks on your system.

---

## 🚀 Overview

This project demonstrates an end-to-end **Voice AI Agent pipeline** that:

- Accepts audio input (WAV/MP3)
- Converts speech to text using Whisper
- Detects user intent using a hybrid (Rule + LLM) approach
- Executes tasks locally (file creation, summarization, etc.)
- Ensures safe execution with confirmation and restrictions

The system is designed to be **fully local (no paid APIs)**, privacy-friendly, and extensible.

---

## 🎯 Key Features

### 🎤 Voice Input
- Upload `.wav` or `.mp3` audio files
- Easily extendable to microphone input

### 🧠 Speech-to-Text (STT)
- Powered by **Whisper (local model)**
- Supports multilingual inputs (basic Hindi/Hinglish)

### 🤖 Intent Detection (Hybrid AI)
- Rule-based logic for reliability
- Local LLM via Ollama (Phi model) for flexibility

### ⚙️ Task Execution
- Create files
- Write code to files
- Summarize text
- General chat fallback

### 🔐 Safety Layer
- File operations restricted to `/output/`
- Prevents system-level damage
- Validation of unsafe inputs

### ⚠️ Human-in-the-Loop
- Confirmation required before execution
- Prevents unintended actions

### 🧠 Memory (Basic)
- Stores previous actions (extendable)

### 📊 Benchmarking
- Measures STT and LLM latency

---

## 🏗️ System Architecture
Audio Input
↓
Speech-to-Text (Whisper)
↓
Language Detection
↓
Intent Planner (Rule + LLM)
↓
Safety Validator
↓
User Confirmation
↓
Task Executor
↓
Output (UI + File System)


---

## ⚙️ Tech Stack

| Component        | Technology |
|----------------|-----------|
| STT            | Whisper (local) |
| LLM            | Ollama (Phi model) |
| Backend        | FastAPI |
| Frontend       | Streamlit |
| Language Detection | langdetect |
| Execution      | Python (OS-safe operations) |

---

## 📂 Project Structure


voice-ai-agent/
│
├── app/main.py
│
├── api/server.py
│
├── core/ orchestrator.py   , planner.py
│
├── stt/ whisper_local.py
│
├── nlp/ summarizer.py  language_detector.py
│
├── tools/ file_manager.py   executor.py
│
├── safety/ validator.py
│
├── memory/ history_store.py
│
├── benchmarking/ metrics.py logger.py
│
├── config/ settings.yaml
│
├── output/        ← files created here
├── logs/          ← logs stored here
│
├── requirements.txt
├── README.md

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Priyalparmar03/voice-ai-agent

cd voice-ai-agent
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install and Run Ollama

Install Ollama → then:

ollama run phi
5️⃣ Start Backend
uvicorn api.server:app --reload
6️⃣ Start UI
streamlit run app/main.py
🧪 Example Usage
🎤 Input:

"Create a file named test.txt"

🧠 System Output:
Intent: create_file
File created in /output/test.txt
⚠️ Safety Design
All file operations restricted to /output/
No overwrite of system files
Path validation
User confirmation required
🧠 Challenges & Solutions
Challenge	Solution
LLM JSON inconsistency	Hybrid rule-based system
Windows encoding error	UTF-8 encoding in subprocess
Low system resources	Switched to lightweight Phi model
Silent UI failure	Debug pipeline + structured response

echnical Article

Published on:
👉 Medium : https://medium.com/@parmarpriyal1603/building-a-multilingual-voice-controlled-ai-agent-with-safety-mechanisms-fully-local-free-6a6c1623f186


🚀 Future Improvements
🎤 Real-time microphone input
🇮🇳 Better Indian language support (Gujarati, Hindi NLP)
🧠 Advanced memory (vector database)
🌐 Deployment (Docker / Cloud)
💬 Chat-style UI


Author

Priyal Parmar
