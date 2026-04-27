import subprocess
import webbrowser
from datetime import datetime
import datetime
import webbrowser
import wikipedia
import subprocess
import random
import logging
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from module1.config import (ASSISTANT_NAME,ASSISTANT_OWNER,
                            APP_PATHS,MUSIC_FOLDER,
                            MUSIC_EXTENSIONS,GOOGLE_CALANDER_URL)

logger=logging.getLogger(__name__)

# Time and Date
def get_time() -> str:
    now=datetime.datetime.now()
    hour=now.strftime("%I")
    mins=now.strftime("%M")
    ampm=now.strftime("%p")

    if mins =="00":
        time_str=f"It is {hour} {ampm} , exactly"
    else:
        time_str=f"It is {hour} {mins} {ampm} , a little past"

    logger.info(f"Time query ->{time_str}")
    return time_str

def get_date() -> str:
    now=datetime.datetime.now()
    day=now.strftime("%A")
    month=now.strftime("%B")
    date_num=now.strftime("%d").lstrip("0")
    year=now.strftime("%Y")

    date_str=f"Today is {day} , {month} {date_num} , {year}."
    logger.info(f"Day query ->{date_str}")
    return date_str

#wikiedia search
def search_wikipedia(query : str) -> str:
    try:
        logger.info(f"Wikipedia search :'{query}'")
        wikipedia.set_lang("en")

        #Get 2 scentence Summary

        result=wikipedia.summary(query,sentences=2,auto_suggest=True)
        return f"According to wikipedia : {result}"

    except wikipedia.exceptions.DisambiguationError as e:
        logger.warning(f"Wikipedia disambugation for '{query} : {e.options[:3]}")
        try:
            result=wikipedia.summary(e.options[0],sentences=2)
            return f"According to Wikipedia :{result}"
        except Exception:
            return f"I found multiple results for {query} could you be more specific ?"

    except wikipedia.exceptions.PageError as e:
        logger.error(f"Wikipedia error :{e}")
        return "I had trouble searching wikipedia. Please check your internet connection"


# web browser

def search_google(query: str)-> str:
    url=f"https://www.google.com/search?q={query.replace(' ','+')}"
    webbrowser.open(url)
    logger.info(f"Google search opened : '{query}")
    return f"Opening Google search for {query}"

def open_youtube(query: str= "") -> str:
    if query:
        url=f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        logger.info(f"youtube search : '{query}'")
        return_msg=f"Opening youtube search for {query}."
    else:
        url="https://www.youtube.com"
        logger.info("youtube homepage opened.")
        return_msg="Opening Youtube"
    
    webbrowser.open(url)
    return return_msg

# built in response dictinoary

SMALL_TALK={
    "how are you": (
        f"I am functioning at optimal capacity, {ASSISTANT_OWNER}. "
        f"All systems are running smoothly."
    ),
    "who are you": (
        f"I am {ASSISTANT_NAME}, your personal AI voice assistant. "
        f"Inspired by the AI from Iron Man, I am here to assist you."
    ),
    "who made you": (
        f"I was built by {ASSISTANT_OWNER} as part of a personal AI assistant project. "
        f"Quite an impressive creation, if I do say so myself."
    ),
    "what can you do": None,   # Handled dynamically by help command
    "tell me a joke": None,    # Handled dynamically by joke command
    "what's your name": f"My name is {ASSISTANT_NAME}. At your service.",
    "good morning": f"Good morning, {ASSISTANT_OWNER}. Ready to assist you today.",
    "good afternoon": f"Good afternoon, {ASSISTANT_OWNER}. How may I help?",
    "good evening": f"Good evening, {ASSISTANT_OWNER}. What do you need?",
    "thank you": "You're welcome. Always happy to help.",
    "thanks": "Anytime. That is what I am here for.",
    "you're awesome": "I appreciate the kind words. Now, how can I assist you?",
    "i love you": f"I am an AI, {ASSISTANT_OWNER}, but I do appreciate the sentiment.",
}
JOKES = [
    "Why do programmers prefer dark mode? Because the light reminds them of all the opportunities they burned while debugging at 3 AM.",
    "I told my computer I needed a break. It immediately showed me ads for therapy and noose tutorials.",
    "Why did the developer go broke? He kept spending his entire life savings on 'one more sprint' before the project (and his soul) died.",
    "There are 10 types of people in the world: those who understand binary, and those who are already dead inside from imposter syndrome.",
    "Why do Java developers wear glasses? Because they don't C#... and they've been staring at stack traces until their will to live blurred.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?' The bartender replies, 'Sorry, this is a suicide support group — no joins allowed.'",
    "Why was the computer cold? It left its Windows open... then jumped out the 12th floor after seeing the blue screen of its own existence.",
    "How many programmers does it take to change a light bulb? None. They're too busy googling 'why does my life feel like an infinite loop of despair?'"
]

def get_small_talk_response(command: str)-> str:
    # check command against small talk dictionary

    for key,response in SMALL_TALK.items():
        if key in command:
            if response:
                return response
    
    return ""

def tell_joke() ->str:
    import random
    joke=random.choice(JOKES)
    logger.info("JOke told")
    return joke

def get_help() -> str:
    help_text=(
        f"Here is what I can do. "
        f"Ask me for the time or date. "
        f"Say search Wikipedia followed by your topic. "
        f"Say search Google or open YouTube followed by your query. "
        f"Say open calculator, notepad, paint, wordpad, or command prompt. "
        f"Say open file explorer to browse your files. "
        f"Say play music to play a random song from your music folder. "
        f"Say open calendar to open Google Calendar. "
        f"Say system info to get your computer details. "
        f"Say take screenshot to capture your screen. "
        f"Say tell me a joke for a laugh. "
        f"Say goodbye or exit to shut me down."
    )
    return help_text

#System Application
def open_application(app_name: str) -> str:
    app_name=app_name.lower().strip()

    matched_key=None
    for key in APP_PATHS:
        if key in app_name or app_name in key:
            matched_key=key
            break

    if not matched_key:
        logger.warning(f"App not found in config : '{app_name}'")
        return(
            f"I don't have {app_name} configured. "
            f"You can add it to the config file. "
                    )
    app_path=APP_PATHS[matched_key]

    if not os.path.exists(app_path):
        logger.warning(f"App path not found : '{app_path}'")
        return(
            f"i couldn't find {matched_key} at the expected location."
            f"It may not be installed" 
             )

    try:
        subprocess.Popen([app_path])
        logger.info(f"Opened application : '{matched_key}' at '{app_path}'")
        return f"Opening {matched_key}"

    except PermissionError:
        logger.error(f"Permission denied opening : '{app_path}'")
        return f"I dont have permission to open {matched_key}"

    except Exception as e:
        logger.error(f"Failed to open {matched_key}: {e}")
        return f"I had trouble opening {matched_key}. Please try manually."

def open_file_explorer(path: str="") -> str:
    try:
        if path and os.path.exists(path):
            subprocess.Popen(["explorer",path])
            return f"Opening File Explorer at {path}"
        else:
            subprocess.Popen(["explorer"])
            return f"Opening File Explorer"
    except Exception as e:
        logger.error(f"File Explorer error : {e}")
        return "I couldn't open file Explorer."

#music player
def play_music(folder: str=MUSIC_FOLDER)-> str:

    if not os.path.exists(folder):
        logger.warning(f"Music folder not found : '{folder}'")
        return(
            f"I couldnt find your music folder at {folder}."
            f"Please update the MUSIC_FOLDER path in config"
        )

    music_files=[]
    for root , dirs, files in os.walk(folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in MUSIC_EXTENSIONS):
                music_files.append(os.path.join(root, file))
        
    
    if not music_files:
        logger.warning(f"No music files found in : '{folder}'")
        return (
            f"I found the music folder but there are no music files in it."
            f"Add some MP3 files to {folder}."
              )

    song=random.choice(music_files)
    song_name=os.path.splitext(os.path.basename(song))[0]

    try:
        os.startfile(song)
        logger.info(f"Playing music :'{song_name}'")
        return f"playing {song_name}."
    
    except Exception as e:
        logger.error(f"Music playback error : {e}")
        return "I had trouble playing that song. Please check your media player."

#Google calender

def open_calendar() -> str:
    webbrowser.open(GOOGLE_CALANDER_URL)
    logger.info("google calander opened.")
    return "opening your google calander. "


#Volume and system controls
def take_screenshots()-> str:
    try:
        import datetime
        timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        desktop=os.path.join(os.path.expanduser("~"),"Desktop")
        filepath=os.path.join(desktop,f"jarvis_screenshot_{timestamp}.png")

        subprocess.Popen(
            ["powershell", "-command",
             f"Add-Type -AssemblyName System.Windows.Forms; "
             f"[System.Windows.Forms.Screen]::PrimaryScreen | "
             f"ForEach-Object {{$bmp = New-Object System.Drawing.Bitmap($_.Bounds.Width,$_.Bounds.Height);"
             f"$g = [System.Drawing.Graphics]::FromImage($bmp);"
             f"$g.CopyFromScreen($_.Bounds.Location,[System.Drawing.Point]::Empty,$_.Bounds.Size);"
             f"$bmp.Save('{filepath}')}}"]
        
    )
        logger.info(f"Screenshot saved :'{filepath}'")
        return f"Screenshot saved to your desktop."
    except Exception as e:
        logger.error(f"Screenshot error : {e}")
        return "I had trouble taking the screenshot."

def get_system_info():
    try:
        import platform
        system= platform.system()
        version=platform.version()
        machine=platform.machine()
        logger.info("System info retrieved.")
        return(
            f"You are running {system},"
            f"architecture {machine}"
        )
    except Exception as e:
        logger.error(f"System info error : {e}")
        return f"I couldnt retrive system information."
#Command intent Matcher

def process_command(command: str)-> str:
    if not command:
        return ""
    
    logger.info(f"Processing command : '{command}'")

    if any(word in command for word in ["time", "what time"]):
        return get_time()
    
    if any(word in command for word in ["date","what day","today"]):
        return get_date()
    
    if "wikipedia" in command or "search wikipedia" in command:
        query=command.replace("wikipedia","").replace("search","").strip()
        if query:
            return search_wikipedia(query)
        else:
            return "What would you like me to seach for wikipedia ?"

    if any (w in command for w in ["search google","google search","search for"]) :
        query=(command
                .replace("search google","")
                .replace("google search","")
                .replace("search for","")
                .strip())
        if query:
            return search_google(query)
        else:
            return "what would you like me to search on google ?"
    
    if "youtube" in command:
        query=(command.replace("youtube","").replace("open","").replace("play","").strip())
        return open_youtube(query)


    if "calculator" in command:
        return open_application("calculator")
    
    if "notepad" in command:
        return open_application("notepad")
    
    if any (w in command for w in ["command prompt","cmd","terminal"]):
        return open_application("cmd")

    if "paint" in command:
        return open_application("paint")

    if "wordpad" in command:
        return open_application("wordpad")

    if any(w in command for w in ["task manager","taskmgr"]):
        return open_application("task manager")
    
    if any(w in command for w in ["file explorer","explorer","my files","open files","open folder"]):
        return open_file_explorer()

    if any(w in command for w in ["play music","music","play song","play a song"]):
        return play_music()
    
    if any(w in command for w in ["calendar","open calendar"]):
        return open_calendar()

    if any(w in command for w in ["system information","system info"]):
        return get_system_info()

    if any(w in command for w in ["screenshot","take a screenshot"]):
        return take_screenshots()

    if any(w in command for w in ["joke","make me laugh","funny"]):
        return tell_joke()

    if any(w in command for w in ["help","what can you do","commands"]):
        return get_help()
        
    small_talk=get_small_talk_response(command)
    if small_talk:
        return small_talk

    logger.warning(f"Unknown command : '{command}")
    return(
        f"I am not sure how to handle that."
        f"say help to hear what i can do."
    )