import pyttsx3

engine = pyttsx3.init('sapi5')  # Windows-specific SAPI5 engine

engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

# List all available voices on your Windows machine
voices = engine.getProperty('voices')
print(f"Found {len(voices)} voices on your system:")
for i, voice in enumerate(voices):
    print(f"  [{i}] {voice.name} — {voice.id}")

# Use voice index 0 by default
engine.setProperty('voice', voices[1].id)

engine.say("Hello. I am AutoMoto, your personal AI assistant.")
engine.say("Nice to meet you.")
engine.runAndWait()

print("TTS test complete!")