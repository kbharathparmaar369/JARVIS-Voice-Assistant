# AutoMoto — Personal AI Voice Assistant System

> An intelligent, voice-controlled personal assistant inspired by AutoMoto.  
> Built with Python — two independent modules demonstrating different AI assistant approaches.

---

## Project Structure

```text
AutoMoto-Voice-Assistant/
│
├── module1/                  # CLI Voice Assistant
│   ├── main.py               # Main event loop
│   ├── speech.py             # listen() and speak() engine
│   ├── commands.py           # All feature functions
│   ├── config.py             # Settings and constants
│   ├── logger.py             # Logging module
│   └── history.py            # Command history tracker
│
├── module2/                  # Web AI Assistant
│   ├── app.py                # Streamlit frontend
│   ├── speech_handler.py     # Voice input handler
│   ├── ai_handler.py         # Gemini AI integration
│   └── config.py             # Module 2 settings
│
├── shared/
│   └── speech_utils.py       # Shared speech utilities
│
├── logs/                     # Auto-generated at runtime
│   ├── automoto.log
│   ├── errors.log
│   └── session.log
│
├── .env                      # API keys (never committed)
├── .gitignore
├── requirements_module1.txt
├── requirements_module2.txt
└── README.md
```

---

## Project Overview

| | Module 1 — AutoMoto CLI | Module 2 — Web AI Assistant |
|---|---|---|
| **Interface** | Command Line | Streamlit Web UI |
| **AI Engine** | Rule-based NLP | Google Gemini 2.5 Flash |
| **Voice Input** | SpeechRecognition + PyAudio | SpeechRecognition + PyAudio |
| **Voice Output** | pyttsx3 (offline SAPI5) | gTTS (Google Text-to-Speech) |
| **Languages** | English | Multilingual |
| **Internet** | Optional | Required |

---

## Setup & Installation

### Prerequisites
- Python 3.11.9
- Windows 10/11
- Working microphone
- Internet connection (for Speech API + Wikipedia)

### Module 1 — CLI Assistant

```bash
# Clone the repo
git clone https://github.com/kbharathparmaar369/JARVIS-Voice-Assistant.git
cd AutoMoto-Voice-Assistant

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements_module1.txt

# Run AutoMoto
python -m module1.main
```

### Module 2 — Web Assistant

```bash
# Install dependencies
pip install -r requirements_module2.txt

# Add your Gemini API key to .env
echo GEMINI_API_KEY=your_key_here > .env

# Run the web app
streamlit run module2/app.py
```

---

## Features

### Module 1 — AutoMoto CLI
- Real-time voice command recognition
- Time and date queries
- Wikipedia search and summarization
- Open system apps: Calculator, Notepad, CMD, Paint, File Explorer
- Play random music from local folder
- Google and YouTube search via browser
- Google Calendar integration
- System information retrieval
- Screenshot capture
- 25+ small talk and personality responses
- Programming jokes and random facts
- Coin flip and dice roll
- Full session logging (3 log files)
- Command history tracking

### Module 2 — Multilingual Web Assistant *(Week 2)*
- Google Gemini 2.5 Flash AI responses
- Voice and text input
- Multilingual support
- Audio response playback and download
- Chat history display
- Production logging

---

## Voice Commands — Module 1

| Category | Command Examples |
|---|---|
| **Time & Date** | "What time is it", "What is today's date" |
| **Wikipedia** | "Search Wikipedia artificial intelligence" |
| **Web** | "Search Google Python tutorials", "Open YouTube lofi" |
| **Apps** | "Open calculator", "Open notepad", "Open paint" |
| **Music** | "Play music", "Play a song" |
| **System** | "System info", "Take screenshot" |
| **Fun** | "Tell me a joke", "Flip a coin", "Roll a dice" |
| **Chat** | "Who are you", "How are you", "Tell me a story" |
| **Control** | "Help", "History", "Goodbye" |

---

## Architecture

```text
User Voice Input
│
▼
SpeechRecognition + PyAudio
│
▼
Command Processor (Intent Matching)
│
┌──┴───────────────────────┐
│                          │
▼                          ▼
Feature Functions         Small Talk
(time, wiki, apps...)    (personality)
│                          │
└──────────┬───────────────┘
│
▼
pyttsx3 TTS
│
▼
Speaker Output
│
▼
Logger + History
```

---

## Tech Stack

- **Language**: Python 3.11+
- **Voice Recognition**: SpeechRecognition, PyAudio
- **Speech Synthesis**: pyttsx3 (Offline), gTTS (Online)
- **AI Models**: Google Gemini (Module 2)
- **Utilities**: Wikipedia API, Webbrowser, Subprocess, Logging

---

## Demo

> 📹 Demo video link here — add after recording

---

## Author

**Bharath**  
Engineering Student  
[GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_USERNAME)

---

## License

MIT License — feel free to use and extend this project.
