# 🤖 JARVIS — CLI Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10.4-FF6B6B?style=for-the-badge)
![pyttsx3](https://img.shields.io/badge/pyttsx3-2.90-4ECDC4?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A voice-controlled personal AI assistant inspired by JARVIS from Iron Man.**  
Built entirely in Python — speaks, listens, and controls your system hands-free.

[Features](#-features) • [Installation](#-installation) • [Commands](#-voice-commands) • [Architecture](#-architecture)

</div>

---

## 📌 Overview

JARVIS CLI is an intelligent, offline-capable voice assistant that runs directly in your terminal. It listens to your spoken commands, processes them through a custom intent engine, and responds with a natural voice using Windows SAPI5.

---

## ✨ Features

- **Voice I/O**: Real-time recognition and offline TTS.
- **System Integration**: Open Windows apps (Calculator, Notepad, etc.)
- **Web & Knowledge**: Wikipedia search, Google/YouTube automation.
- **Personality**: 15 programming jokes, 10 facts, and small talk.
- **Logging**: Detailed session logs and command history.

---

## 🛠️ Installation

### Step 1 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements_module1.txt
```

### Step 3 — Run JARVIS
```bash
python main.py
```

---

## 🎙️ Voice Commands

| Category | Say This | What Happens |
|---|---|---|
| **Wikipedia** | *"Search Wikipedia [topic]"* | Speaks 2-sentence summary |
| **Apps** | *"Open calculator"* | Launches Calculator |
| **Music** | *"Play music"* | Plays random song |
| **Fun** | *"Tell me a joke"* | Tells a programming joke |
| **Control** | *"Help"* | Lists all commands |
| **Control** | *"Goodbye"* | Graceful shutdown |

---

## 🏗️ Architecture

```
User Voice Input → SpeechRecognition → Intent Matcher → Feature Execution → pyttsx3 (SAPI5)
```

---

## 📊 Test Results (Day 6 Hardening)

```
=======================================================
  JARVIS MODULE 1 — FINAL TEST SUITE
=======================================================
  Score: 45/45 — 100% ✅
=======================================================
```

---

<div align="center">
  <sub>Built with ❤️ and Python · Inspired by JARVIS from Iron Man</sub>
</div>
