import logging
import logging
import logging
import logging
import logging
import logging
import speech_recognition as sr
import pyttsx3
import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from module1.config import(
    ASSISTANT_NAME,TTS_ENGINE,TTS_RATE,
    TTS_VOLUME,TTS_VOICE_INDEX,SR_AMBIENT_DURATION,
    SR_ENERGY_THRESHOLD,SR_LISTEN_TIMEOUT,SR_PAUSE_THRESHOLD,
    SR_PHRASE_LIMIT,LOG_FILE
)


#loggiing setup
os.makedirs("logs",exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger(__name__)

#TTS Engine initilization

def init_tts_engine():
    try:
        engine=pyttsx3.init(TTS_ENGINE)
        engine.setProperty('rate',TTS_RATE)
        engine.setProperty('volume',TTS_VOLUME)

        voices=engine.getProperty('voices')
    
        if voices:
            index=TTS_VOICE_INDEX if TTS_VOICE_INDEX < len(voices) else 0
            engine.setProperty('voice',voices[index].id)
            logger.info(f"TTS voice set to :{voices[index].name}")
        else:
            logger.warning("No TTS voices found on this system. ")

        return engine

    except Exception as e:
        logger.error(f"TTS engine initilization failed : {e}")
        raise


_tts_engine=init_tts_engine()

#converts text to speech
def speak(text: str)-> None:
    global _tts_engine
    if not text or not text.strip():
        logger.warning("speak() called with empty text -skipping")
        return
    
    try:
        print(f"[AutoMoto]: {text}")
        logger.info(f"Speaking : {text}")
        _tts_engine.say(text)
        _tts_engine.runAndWait()
        
    except RuntimeError as e:
        logger.error(f"TTS Runtime Error: {e}")

       
        _tts_engine=init_tts_engine()
        _tts_engine.say(text)
        _tts_engine.runAndWait()

    except Exception as e:
        logger.error(f"speak () failed : {e}")

#listen

def listen() ->str:
    #listen for the voice command from the microphone
    recognizer=sr.Recognizer()

    recognizer.energy_threshold=SR_ENERGY_THRESHOLD
    recognizer.pause_threshold=SR_PAUSE_THRESHOLD
    recognizer.dynamic_energy_threshold=True

    with sr.Microphone() as source:
        try:
            print("\n [AutoMoto] : Listening..")
            logger.info("Listening for command..")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=SR_AMBIENT_DURATION
            )

            #listen for the speech
            audio=recognizer.listen(
                source,
                timeout=SR_LISTEN_TIMEOUT,
                phrase_time_limit=SR_PHRASE_LIMIT
            )

            print("[AutoMoto]: Recognizing..")
            logger.info("Recognizing audio..")

            command=recognizer.recognize_google(audio)
            command=command.lower().strip()

            print(f"[YOU]: {command}")
            logger.info(f"Recognized : '{command}'")

            return command
        except sr.WaitTimeoutError:
            logger.warning("Listen timeout -no speech detected.")
            speak("I didn't hear anything . please try again ")
            return ""
        
        except sr.RequestError as e:
            logger.error(f"Google Speech API error : {e}")
            speak("I am having trouble connecting to the speech service . check your internet. ")
            return ""

        except Exception as e:
            logger.error(f"listen() unexpected error : {e}")
            return ""


#greeting Helper

def get_time_greeting()-> str:
    from datetime import datetime
    hour=datetime.now().hour

    if 5<=hour <12:
        return "good morning"
    elif 12<= hour<17:
        return "good afternoon"
    elif 17<= hour <21:
        return "good evening"

    else:
        return "Good night"


def greet_user() -> None:
    greeting=get_time_greeting()
    message=(
        f"{greeting},{ASSISTANT_NAME} is online and ready. "
        f"All system are operational. How many i assist you ?"
    )

    speak(message)