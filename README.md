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
