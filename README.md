# 🤖 AutoMoto — CLI Voice Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10.4-FF6B6B?style=for-the-badge)
![pyttsx3](https://img.shields.io/badge/pyttsx3-2.90-4ECDC4?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A voice-controlled personal AI assistant inspired by JARVIS from Iron Man.**  
Built entirely in Python — speaks, listens, and controls your system hands-free.

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Commands](#-voice-commands) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack)

</div>

---

## 📌 Overview

AutoMoto is an intelligent, offline-capable voice assistant that runs directly in your terminal. It listens to your spoken commands, processes them through a custom intent engine, and responds with a natural voice using Windows SAPI5 — no cloud AI subscription required.

This is **Project 1** of a two-part AI assistant system. [Project 2 →](https://github.com/kbharathparmaar369/Multilingual-AI-Web-Assistant) is a web-based assistant powered by Google Gemini AI.

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
- 25+ small talk responses with an AutoMoto personality
- 15 programming jokes
- 10 random interesting facts
- Coin flip and dice roll
- Graceful handling of compliments, insults, and philosophical questions

### 📋 Production-Grade Logging
- 3 separate log files: main log, error log, session log
- Every command and response recorded with timestamps
- In-memory command history (last 10 commands)
- History playback via voice: *"What did I say?"*

---

## 📹 Demo

> 🎬 **[Watch the demo video here](#)** ← *(add your YouTube/Loom link)*

```
$ python main.py

╔══════════════════════════════════════════════════════╗
║        AutoMoto — PERSONAL AI VOICE ASSISTANT        ║
║                    MODULE 1 — CLI                    ║
╠══════════════════════════════════════════════════════╣
║  Say 'help'     → hear all available commands        ║
║  Say 'history'  → hear your recent commands          ║
║  Say 'goodbye'  → shut down AutoMoto                 ║
╚══════════════════════════════════════════════════════╝

  [AutoMoto] » Good afternoon. AutoMoto is online and ready.
              All systems are operational. How may I assist you, Bharath?

  [AutoMoto] » Listening...
  [YOU]       » search wikipedia artificial intelligence
  [AutoMoto] » According to Wikipedia: Artificial intelligence is
              intelligence demonstrated by machines...

  [AutoMoto] » Listening...
  [YOU]       » open calculator
  [AutoMoto] » Opening calculator.

  [AutoMoto] » Listening...
  [YOU]       » tell me a joke
  [AutoMoto] » Why do programmers prefer dark mode?
              Because light attracts bugs.
```

---

## 🛠️ Installation

### Prerequisites
- Windows 10 or 11
- Python 3.11.9 ([Download](https://www.python.org/downloads/release/python-3119/))
- Working microphone
- Internet connection (for Speech API + Wikipedia)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/kbharathparmaar369/AutoMoto-CLI-Voice-Assistant.git
cd AutoMoto-CLI-Voice-Assistant
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ **PyAudio on Windows** — if `pip install pyaudio` fails:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### Step 4 — Configure (Optional)
Open `config.py` and update:
```python
ASSISTANT_OWNER = "Bharath"      # Your name
TTS_VOICE_INDEX = 0              # 0 = David (male), 1 = Zira (female)
MUSIC_FOLDER    = r"C:\Users\YourName\Music"   # Your music folder
```

### Step 5 — Run AutoMoto
```bash
python main.py
```

---

## 🎙️ Voice Commands

| Category | Say This | What Happens |
|---|---|---|
| **Time & Date** | *"What time is it"* | Speaks current time |
| **Time & Date** | *"What is today's date"* | Speaks current date |
| **Wikipedia** | *"Search Wikipedia [topic]"* | Speaks 2-sentence summary |
| **Google** | *"Search Google [query]"* | Opens Google search |
| **YouTube** | *"Open YouTube [query]"* | Opens YouTube search |
| **Apps** | *"Open calculator"* | Launches Calculator |
| **Apps** | *"Open notepad"* | Launches Notepad |
| **Apps** | *"Open command prompt"* | Launches CMD |
| **Apps** | *"Open paint"* | Launches MS Paint |
| **Apps** | *"Open file explorer"* | Launches File Explorer |
| **Music** | *"Play music"* | Plays random song from folder |
| **Calendar** | *"Open calendar"* | Opens Google Calendar |
| **System** | *"System info"* | Speaks OS details |
| **System** | *"Take screenshot"* | Captures and saves screen |
| **Fun** | *"Tell me a joke"* | Tells a programming joke |
| **Fun** | *"Tell me a fact"* | Shares an interesting fact |
| **Fun** | *"Flip a coin"* | Heads or tails |
| **Fun** | *"Roll a dice"* | Random 1–6 |
| **Fun** | *"Tell me a story"* | AutoMoto tells a short story |
| **Chat** | *"Who are you"* | AutoMoto introduces itself |
| **Chat** | *"How are you"* | AutoMoto status report |
| **Chat** | *"What is the meaning of life"* | Philosophical response |
| **Control** | *"Help"* | Lists all commands |
| **Control** | *"What did I say"* | Recaps recent commands |
| **Control** | *"Goodbye"* | Graceful shutdown |

---

## 🏗️ Architecture

```
User Voice Input (Microphone)
         │
         ▼
  SpeechRecognition
  + PyAudio
  + Google Speech API
         │
         ▼
    listen()                    ← speech.py
         │
         ▼
  process_command()             ← commands.py
         │
    ┌────┴─────────────────────────────────────┐
    │                                          │
    ▼                                          ▼
Feature Functions                      Small Talk Engine
  • get_time()                           • SMALL_TALK dict
  • get_date()                           • tell_joke()
  • search_wikipedia()                   • tell_fact()
  • search_google()                      • flip_coin()
  • open_youtube()                       • roll_dice()
  • open_application()
  • play_music()
  • open_calendar()
  • get_system_info()
  • take_screenshot()
    │                                          │
    └────────────┬─────────────────────────────┘
                 │
                 ▼
            speak()                     ← speech.py
                 │
                 ▼
    pyttsx3 (SAPI5) → Speaker Output
                 │
                 ▼
    Logger + Command History            ← logger.py / history.py
```

---

## 📁 Project Structure

```
AutoMoto-CLI-Voice-Assistant/
│
├── main.py               ← Main event loop — entry point
├── speech.py             ← listen() and speak() engine
├── commands.py           ← All 30+ feature functions + intent matcher
├── config.py             ← All settings and constants
├── logger.py             ← 3-file logging system
├── history.py            ← In-memory command history tracker
│
├── logs/                 ← Auto-created at runtime
│   ├── automoto.log      ← All events
│   ├── errors.log        ← Errors only
│   └── session.log       ← Per-session command history
│
├── requirements.txt      ← Locked dependency versions
└── README.md
```

---

## 📦 Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.11.9 | Core language |
| **SpeechRecognition** | 3.10.4 | Mic input → text |
| **PyAudio** | 0.2.14 | Audio stream handling |
| **pyttsx3** | 2.90 | Offline text-to-speech (SAPI5) |
| **Wikipedia** | 1.4.0 | Knowledge search |
| **comtypes** | 1.4.1 | Windows SAPI5 dependency |
| **pywin32** | 306 | Windows OS integration |
| **subprocess** | built-in | Launch system applications |
| **webbrowser** | built-in | Browser automation |
| **logging** | built-in | Production-grade logging |

---

## 📊 Test Results

```
=======================================================
  AutoMoto MODULE 1 — FINAL TEST SUITE
=======================================================
  Section 1  : Time & Date          4/4  ✅
  Section 2  : Wikipedia            4/4  ✅
  Section 3  : Web Browser          4/4  ✅
  Section 4  : System Apps          5/5  ✅
  Section 5  : Music & Calendar     4/4  ✅
  Section 6  : System Utilities     2/2  ✅
  Section 7  : Personality Identity 7/7  ✅
  Section 8  : Greetings & Chat     7/7  ✅
  Section 9  : Fun & Games          6/6  ✅
  Section 10 : Edge Cases           4/4  ✅
  Section 11 : Command History      1/1  ✅
  Section 12 : Log Files            3/3  ✅
=======================================================
  Score: 45/45 — 100% ✅
=======================================================
```

---

## 📝 Log Output Sample

```
# session.log
============================================================
  SESSION STARTED: 2024-01-15 14:32:01
============================================================
  [14:32:04] CMD : search wikipedia artificial intelligence
  [14:32:04] RESP: According to Wikipedia: Artificial intell...
  ────────────────────────────────────────────────────────
  [14:32:18] CMD : open calculator
  [14:32:18] RESP: Opening calculator.
  ────────────────────────────────────────────────────────
  [14:32:30] CMD : tell me a joke
  [14:32:30] RESP: Why do programmers prefer dark mode?...
  ────────────────────────────────────────────────────────
  SESSION ENDED:   2024-01-15 14:35:22
============================================================
```

---

## 🔧 Configuration Reference

All settings live in `config.py`:

```python
# Identity
ASSISTANT_NAME  = "AutoMoto"
ASSISTANT_OWNER = "Bharath"

# Voice
TTS_RATE        = 180          # Words per minute
TTS_VOICE_INDEX = 0            # 0 = David (male), 1 = Zira (female)

# Microphone
SR_LISTEN_TIMEOUT  = 5         # Seconds to wait for speech
SR_PHRASE_LIMIT    = 10        # Max length of one command

# Music
MUSIC_FOLDER    = r"C:\Users\YourName\Music"

# History
MAX_HISTORY     = 10           # Commands kept in memory
```

---

## 🚀 What's Next

This is **Project 1** of a two-part system.

**[Project 2 — Multilingual AI Web Assistant →](https://github.com/kbharathparmaar369/Multilingual-AI-Web-Assistant)**

- Google Gemini 2.5 Flash AI brain
- Streamlit web interface
- 8-language support
- Audio response download

---

## 🤝 Contributing

Pull requests are welcome. For major changes please open an issue first.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/new-command`
3. Commit your changes: `git commit -m "Add weather command"`
4. Push and open a PR

---

## 👨‍💻 Author

**Bharath Kumar**
Engineering Student

[![GitHub](https://img.shields.io/badge/GitHub-kbharathparmaar369-181717?style=flat&logo=github)](https://github.com/kbharathparmaar369)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/kbharathparmaar369)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with ❤️ and Python by Bharath · Inspired by JARVIS from Iron Man</sub>
</div>
