import speech_recognition as sr

recognizer = sr.Recognizer()

print("Testing microphone... Speak something!")

with sr.Microphone() as source:
    print("Adjusting for ambient noise... please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening now — say something:")

    try:
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio)
        print(f"SUCCESS - You said: '{text}'")
    except sr.WaitTimeoutError:
        print("TIMEOUT — no speech detected. Check mic permissions.")
    except sr.UnknownValueError:
        print("Could not understand audio. Speak louder/clearer.")
    except sr.RequestError as e:
        print(f"API error: {e}. Check your internet connection.")