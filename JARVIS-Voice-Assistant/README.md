# 🤖 AutoMoto — Multi-Module AI Assistant System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

**A powerful, two-part AI voice assistant system built for efficiency.**  
One offline CLI engine + One advanced Gemini-powered Web UI.

[Module 1 (CLI)](./module1/) • [Module 2 (Web)](./module2/) • [Setup](#-installation) • [Architecture](#-system-architecture)

</div>

---

## 📌 Project Overview

This repository contains two independent AI assistant modules, each showcasing a different approach to speech interaction and intelligence.

| | Module 1 — CLI Assistant | Module 2 — Web Assistant |
|---|---|---|
| **Branding** | AutoMoto CLI | AutoMoto Web AI |
| **Interface** | Command Line (CLI) | Streamlit Web UI |
| **Brain** | Intent-based Matching | Google Gemini 2.5 Flash |
| **Speech** | Offline (SAPI5) | Online (gTTS) |
| **Best For** | System Control & Speed | Reasoning & Translation |

---

## 📂 System Structure

```
AutoMoto-Voice-Assistant/
│
├── module1/                  # CLI Voice Assistant (Offline)
│   ├── main.py               # Entry point
│   └── README.md             # Detailed CLI Guide
│
├── module2/                  # Web AI Assistant (Gemini)
│   ├── app.py                # Streamlit UI
│   └── README.md             # Detailed Web Guide
│
├── shared/                   # Shared utilities
├── logs/                     # System logs
└── requirements_module1.txt  # Dependencies
```

---

## 🛠️ Installation

### Step 1 — Setup Module 1 (CLI)
```bash
# Install dependencies
pip install -r requirements_module1.txt

# Run the assistant
python -m module1.main
```

### Step 2 — Setup Module 2 (Web)
```bash
# Install dependencies
pip install -r requirements_module2.txt

# Add your GEMINI_API_KEY to .env
# Run the web app
streamlit run module2/app.py
```

---

## 🏗️ System Architecture

1.  **Input**: User speaks via microphone.
2.  **Recognition**: SpeechRecognition converts audio to text.
3.  **Processing**: 
    *   **Module 1**: Direct intent matching for system apps/commands.
    *   **Module 2**: Google Gemini AI for complex reasoning.
4.  **Output**: AutoMoto responds with clear, synthesized speech.

---

## 👨‍💻 Author

**Bharath**  
Engineering Student  
[GitHub](https://github.com/kbharathparmaar369) · [LinkedIn](https://linkedin.com/in/kbharathparmaar369)

---

## 📄 License
MIT License

<div align="center">
  <sub>Built with ❤️ and Python · © 2024 AutoMoto</sub>
</div>
