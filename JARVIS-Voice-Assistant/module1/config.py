import os
# Assistant identity
ASSISTANT_NAME = "Jarvis"
ASSISTANT_OWNER = "Sir"          

# Text-to-Speech settings
TTS_ENGINE     = "sapi5"         # Windows SAPI5
TTS_RATE       = 180             # Words per minute (170-190 feels natural)
TTS_VOLUME     = 1.0             # 0.0 to 1.0
TTS_VOICE_INDEX = 0              # 0 = Microsoft David (male), 1 = Zira (female)

# Speech Recognition settings
SR_ENERGY_THRESHOLD   = 300      # Mic sensitivity (lower = more sensitive)
SR_PAUSE_THRESHOLD    = 0.8      # Seconds of silence before phrase ends
SR_AMBIENT_DURATION   = 1        # Seconds to sample ambient noise on startup
SR_LISTEN_TIMEOUT     = 5        # Seconds to wait for speech to start
SR_PHRASE_LIMIT       = 10       # Max seconds for a single phrase

# Logging
LOG_FILE = "logs/jarvis.log"
MAX_HISTORY = 10

APP_PATHS = {
    "calculator"  : r"C:\Windows\System32\calc.exe",
    "notepad"     : r"C:\Windows\System32\notepad.exe",
    "cmd"         : r"C:\Windows\System32\cmd.exe",
    "paint"       : r"C:\Windows\System32\mspaint.exe",
    "wordpad"     : r"C:\Program Files\Windows NT\Accessories\wordpad.exe",
    "task manager": r"C:\Windows\System32\Taskmgr.exe",
    "file explorer": r"C:\Windows\explorer.exe",
}

MUSIC_FOLDER=os.path.join(os.path.expanduser("~"),"Music")
MUSIC_EXTENSIONS=[".mp3",".wav",".m4a",".flac",".wma"]

GOOGLE_CALANDER_URL="https://calendar.google.com"