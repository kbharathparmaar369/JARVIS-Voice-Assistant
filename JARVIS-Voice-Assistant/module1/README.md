# 🤖 AutoMoto — CLI Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10.4-FF6B6B?style=for-the-badge)
![pyttsx3](https://img.shields.io/badge/pyttsx3-2.90-4ECDC4?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A voice-controlled personal AI assistant named AutoMoto.**  
Built entirely in Python — speaks, listens, and controls your system hands-free.

[Features](#-features) • [Installation](#-installation) • [Commands](#-voice-commands) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack)

</div>

---

## 📌 Overview

AutoMoto CLI is an intelligent, offline-capable voice assistant that runs directly in your terminal. It listens to your spoken commands, processes them through a custom intent engine, and responds with a natural voice using Windows SAPI5 — no cloud AI subscription required.

This is **Project 1** of a two-part AI assistant system. **Project 2** is a web-based assistant powered by Google Gemini AI.

---

## ✨ Features

### 🎤 Voice I/O
- Real-time speech recognition via Google Speech API
- Offline text-to-speech using Windows SAPI5 (pyttsx3)
- Auto ambient noise adjustment for accurate recognition
- Graceful error handling for mic issues, timeouts, and API failures

### 🧠 Smart Command Processing
- Custom intent matcher — no ML model required
- 30+ built-in voice commands across 9 categories
- Natural language flexibility — multiple phrasings per command
- Unknown command fallback with helpful suggestions

### 💻 System Integration
- Open Windows apps by voice: Calculator, Notepad, Paint, CMD, File Explorer
- Google and YouTube search via browser
- Play random music from your local music folder
- Take screenshots hands-free
- Get live system information

### 🌐 Web & Knowledge
- Wikipedia search with 2-sentence spoken summary
- Disambiguation handling for ambiguous queries
- Google Calendar integration via browser

### 🎭 Personality Layer
- 25+ small talk responses with a professional yet friendly personality
- 15 programming jokes
- 10 random interesting facts
- Coin flip and dice roll

### 📋 Production-Grade Logging
- 3 separate log files: main log, error log, session log
- Every command and response recorded with timestamps
- In-memory command history (last 10 commands)
- History playback via voice: *"What did I say?"*

---

## 🛠️ Installation

### Prerequisites
- Windows 10 or 11
- Python 3.11.9
- Working microphone
- Internet connection (for Speech API + Wikipedia)

### Step 1 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements_module1.txt
```

### Step 3 — Run AutoMoto
```bash
python main.py
```

---

## 🎙️ Voice Commands

| Category | Say This | What Happens |
|---|---|---|
| **Wikipedia** | *"Search Wikipedia [topic]"* | Speaks 2-sentence summary |
| **Google** | *"Search Google [query]"* | Opens Google search |
| **YouTube** | *"Open YouTube [query]"* | Opens YouTube search |
| **Apps** | *"Open calculator"* | Launches Calculator |
| **Music** | *"Play music"* | Plays random song from folder |
| **Calendar** | *"Open calendar"* | Opens Google Calendar |
| **System** | *"System info"* | Speaks OS details |
| **System** | *"Take screenshot"* | Captures and saves screen |
| **Fun** | *"Tell me a joke"* | Tells a programming joke |
| **Fun** | *"Tell me a fact"* | Shares an interesting fact |
| **Control** | *"Help"* | Lists all commands |
| **Control** | *"What did I say"* | Recaps recent commands |
| **Control** | *"Goodbye"* | Graceful shutdown |

---

## 🏗️ Architecture

```
User Voice Input (Microphone) → SpeechRecognition → process_command() → Feature Execution → speak() → pyttsx3 (SAPI5)
```

---

## 📊 Test Results

```
=======================================================
  AutoMoto MODULE 1 — FINAL TEST SUITE
=======================================================
  Score: 45/45 — 100% ✅
=======================================================
```

---

## 📦 Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11.9** | Core language |
| **SpeechRecognition** | Mic input → text |
| **pyttsx3** | Offline text-to-speech (SAPI5) |
| **Wikipedia API** | Knowledge search |
| **Logging** | Production-grade logging |

---

<div align="center">
  <sub>Built with ❤️ and Python · By Bharath</sub>
</div>
