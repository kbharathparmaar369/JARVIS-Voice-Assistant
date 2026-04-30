import logging
import speech_recognition as sr
import pyttsx3
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from module1.config import(
    ASSISTANT_NAME, TTS_ENGINE, TTS_RATE,
    TTS_VOLUME, TTS_VOICE_INDEX, SR_AMBIENT_DURATION,
    SR_ENERGY_THRESHOLD, SR_LISTEN_TIMEOUT, SR_PAUSE_THRESHOLD,
    SR_PHRASE_LIMIT
)
from module1.logger import setup_logger

logger = setup_logger("speech")


# TTS ENGINE (Text-to-Speech)


def _build_tts_engine() -> pyttsx3.Engine:
    """Initializes and returns the TTS engine with config settings."""
    try:
        engine = pyttsx3.init(TTS_ENGINE)
        engine.setProperty("rate", TTS_RATE)
        engine.setProperty("volume", TTS_VOLUME)

        voices = engine.getProperty("voices")
        if voices:
            index = TTS_VOICE_INDEX if TTS_VOICE_INDEX < len(voices) else 0
            engine.setProperty("voice", voices[index].id)
            logger.info(f"TTS voice set to: {voices[index].name}")
        else:
            logger.warning("No TTS voices found on this system.")
        
        return engine
    except Exception as e:
        logger.error(f"TTS engine initialization failed: {e}")
        raise

# Global engine instance
_engine = _build_tts_engine()

def speak(text: str, retries: int = 2) -> None:
    """Converts text to speech with a retry mechanism for robustness."""
    global _engine
    
    if not text or not text.strip():
        return

    print(f"\n [AutoMoto] » {text}")
    logger.info(f"Speaking: {text[:80]}...")

    for attempt in range(retries + 1):
        try:
            _engine.say(text)
            _engine.runAndWait()
            return  # Success!

        except RuntimeError as e:
            logger.warning(f"TTS RuntimeError (attempt {attempt+1}): {e}")
            try:
                _engine.stop()
            except Exception:
                pass
            time.sleep(0.3)
            # Rebuild engine for next attempt
            _engine = _build_tts_engine()

        except Exception as e:
            logger.error(f"speak() failed: {e}")
            break

    logger.error("speak() failed after all retries.")

# SPEECH RECOGNITION (STT)


def _build_recognizer() -> sr.Recognizer:
    """Configures and returns a Speech Recognition object."""
    r = sr.Recognizer()
    r.energy_threshold = SR_ENERGY_THRESHOLD
    r.pause_threshold = SR_PAUSE_THRESHOLD
    r.dynamic_energy_threshold = True
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_ratio = 1.5
    return r

def listen() -> str:
    """Listens for audio input and converts it to text using Google STT."""
    recognizer = _build_recognizer()
    
    with sr.Microphone() as source:
        try:
            print("\n [AutoMoto] » Listening...", end="", flush=True)
            
            recognizer.adjust_for_ambient_noise(
                source, 
                duration=SR_AMBIENT_DURATION
            )

            audio = recognizer.listen(
                source, 
                timeout=SR_LISTEN_TIMEOUT, 
                phrase_time_limit=SR_PHRASE_LIMIT
            )

            print(" Recognizing...", end="", flush=True)
            command = recognizer.recognize_google(audio).lower().strip()
            
            print(f"\n [YOU] : {command}")
            logger.info(f"Recognized: '{command}'")
            return command

        except sr.WaitTimeoutError:
            logger.warning("Listen timeout - no speech detected.")
            return ""
        
        except sr.UnknownValueError:
            print("\n [AutoMoto] » Could not understand audio.")
            logger.warning("Google Speech could not understand audio.")
            speak("I'm sorry, I didn't catch that. Could you repeat it?")
            return ""
            
        except sr.RequestError as e:
            logger.error(f"Google Speech API error: {e}")
            speak("I'm having trouble connecting to the speech service. Check your internet.")
            return ""

        except OSError as e:
            print("\n [AutoMoto] » Microphone error.")
            logger.error(f"Microphone OS error: {e}")
            speak("I cannot access your microphone. Please check your system settings.")
            return ""

        except Exception as e:
            logger.error(f"listen() unexpected error: {e}")
            return ""


# GREETING LOGIC


def get_time_greeting() -> str:
    """Returns a greeting string based on the current hour of the day."""
    from datetime import datetime
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Hello"

def greet_user() -> None:
    """Greets the user upon startup."""
    greeting = get_time_greeting()
    message = (
        f"{greeting}. {ASSISTANT_NAME} is online and ready. "
        f"All systems are operational. How may I assist you?"
    )
    speak(message)