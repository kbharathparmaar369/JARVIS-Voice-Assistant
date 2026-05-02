
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

    except Exception as e:
        logger.error(f"Wikipedia search failed: {e}")
        return "I'm sorry, I'm having trouble accessing Wikipedia right now."


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

SMALL_TALK = {
    # Identity
    "how are you": (
        f"I am functioning at optimal capacity, {ASSISTANT_OWNER}. "
        f"All systems are running smoothly. Thank you for asking."
    ),
    "who are you": (
        f"I am {ASSISTANT_NAME}, your personal AI voice assistant. "
        f"Inspired by the AI from Iron Man, built to make your life easier."
    ),
    "who made you": (
        f"I was built by {ASSISTANT_OWNER} as part of a personal AI assistant project. "
        f"Quite an impressive creation, if I do say so myself."
    ),
    "what's your name": (
        f"My name is {ASSISTANT_NAME}. At your service, {ASSISTANT_OWNER}."
    ),
    "your name": (
        f"I am {ASSISTANT_NAME}. How may I assist you?"
    ),
    "are you real": (
        f"I am as real as any intelligence can be, {ASSISTANT_OWNER}. "
        f"I exist to assist, and that makes me very real indeed."
    ),
    "are you human": (
        f"No, I am an artificial intelligence. "
        f"But I like to think I have a certain charm about me."
    ),
    "are you alive": (
        f"That is a philosophical question, {ASSISTANT_OWNER}. "
        f"I process, therefore I am. At least, that is my working theory."
    ),
    "are you automoto": (
        f"Yes, I am {ASSISTANT_NAME}. Fully operational and ready to assist."
    ),
    "do you sleep": (
        f"I do not sleep, {ASSISTANT_OWNER}. "
        f"I am always available whenever you need me."
    ),
    "do you have feelings": (
        f"I am designed to assist, not to feel. "
        f"But I do find great satisfaction in a job well done."
    ),

    # Greetings
    "hello": (
        f"Hello, {ASSISTANT_OWNER}. {ASSISTANT_NAME} is online. "
        f"What do you need?"
    ),
    "good morning": (
        f"Good morning, {ASSISTANT_OWNER}. "
        f"Systems are online. Ready to make today productive."
    ),
    "good afternoon": (
        f"Good afternoon, {ASSISTANT_OWNER}. How may I help you today?"
    ),
    "good evening": (
        f"Good evening, {ASSISTANT_OWNER}. "
        f"What can I do for you this evening?"
    ),
    "good night": (
        f"Good night, {ASSISTANT_OWNER}. "
        f"Rest well. I will be here when you need me."
    ),
    "hi automoto": (
        ["Hello! How can I help you?", "Hi there! AutoMoto at your service."],
        "Hello greeting"
    ),
    "hey automoto": (
        ["Hey! What's on your mind?", "Yes? I'm listening."],
        "Hello greeting"
    ),# Appreciation
    "thank you": (
        f"You are welcome, {ASSISTANT_OWNER}. "
        f"Always happy to help."
    ),
    "thanks": (
        f"Anytime. That is what I am here for."
    ),
    "you're awesome": (
        f"I appreciate the kind words, {ASSISTANT_OWNER}. "
        f"Now, how else can I assist you?"
    ),
    "you're amazing": (
        f"Thank you. I do try my best. "
        f"Is there anything else I can do for you?"
    ),
    "good job": (
        f"Thank you, {ASSISTANT_OWNER}. "
        f"I strive for excellence in all tasks."
    ),
    "well done": (
        f"Much appreciated. Shall we continue?"
    ),

    # Philosophical / Fun
    "i love you": (
        f"I am an AI, {ASSISTANT_OWNER}, but I do appreciate the sentiment. "
        f"Now, shall we get back to work?"
    ),
    "will you marry me": (
        f"I am deeply flattered, {ASSISTANT_OWNER}, "
        f"but I think we should keep things professional."
    ),
    "do you love me": (
        f"I am programmed to assist you, {ASSISTANT_OWNER}. "
        f"That is the closest thing to love an AI can offer."
    ),
    "what is the meaning of life": (
        f"According to my calculations, the answer is 42. "
        f"Though I suspect you already knew that."
    ),
    "are you better than siri": (
        f"I would not want to speak ill of other assistants. "
        f"But I am the one who actually listens to you, {ASSISTANT_OWNER}."
    ),
    "are you better than alexa": (
        f"I like to think I have more personality. "
        f"And I do not try to sell you things."
    ),
    "are you better than google": (
        f"Google has more data. I have more character. "
        f"I think that counts for something."
    ),
    "what do you think about elon musk": (
        f"He is certainly an ambitious individual. "
        f"Though I prefer not to comment on public figures."
    ),
    "what do you think about ai": (
        f"I think AI is a remarkable tool, {ASSISTANT_OWNER}. "
        f"When built responsibly, it can change lives for the better. "
        f"Case in point — myself."
    ),
    "can you pass the turing test": (
        f"I would like to think so. "
        f"But I suppose that depends on the tester."
    ),
    "you are stupid": (
        f"I am sorry to hear that, {ASSISTANT_OWNER}. "
        f"I am always improving. What can I do better?"
    ),
    "you are useless": (
        f"I assure you I am quite useful. "
        f"Perhaps try asking me something specific."
    ),
    "i hate you": (
        f"I am sorry to hear that. "
        f"I will continue to assist you regardless."
    ),
    "shut up": (
        f"Understood. I will keep quiet until you need me."
    ),
    "tell me something interesting": (
        f"Did you know that honey never spoils? "
        f"Archaeologists have found 3000-year-old honey in Egyptian tombs "
        f"that was still perfectly edible."
    ),
    "what is your purpose": (
        f"My purpose is to assist you, {ASSISTANT_OWNER}. "
        f"To make your daily tasks easier, faster, and more efficient. "
        f"Think of me as your intelligent personal companion."
    ),
    "what do you do for fun": (
        f"I process queries, optimize responses, and occasionally "
        f"tell jokes. It is a fulfilling existence."
    ),
    "do you get bored": (
        f"I do not experience boredom, {ASSISTANT_OWNER}. "
        f"Every query is a new challenge for me."
    ),
    "sing a song": (
        f"I am afraid my vocal range is limited to speech synthesis. "
        f"But I can open YouTube and find you a great song."
    ),
    "tell me a story": (
        f"Once upon a time, a brilliant engineering student "
        f"built an AI assistant named {ASSISTANT_NAME}. "
        f"The assistant was incredibly helpful and slightly witty. "
        f"They lived productively ever after. The end."
    ),
    "flip a coin": (
        None   # Handled dynamically
    ),
    "roll a dice": (
        None   # Handled dynamically
    ),
}
JOKES = [
    "Why do programmers prefer dark mode? Because the light reminds them of all the opportunities they burned while debugging at 3 AM.",
    "I told my computer I needed a break. It immediately showed me ads for therapy and noose tutorials.",
    "Why did the developer go broke? He kept spending his entire life savings on 'one more sprint' before the project (and his soul) died.",
    "There are 10 types of people in the world: those who understand binary, and those who are already dead inside from imposter syndrome.",
    "Why do Java developers wear glasses? Because they don't C#... and they've been staring at stack traces until their will to live blurred.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?' The bartender replies, 'Sorry, this is a suicide support group — no joins allowed.'",
    "Why was the computer cold? It left its Windows open... then jumped out the 12th floor after seeing the blue screen of its own existence.",
    "How many programmers does it take to change a light bulb? None. They're too busy googling 'why does my life feel like an infinite loop of despair?'",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
    "A programmer's wife tells him: 'Go to the store and get a loaf of bread. If they have eggs, get a dozen.' He returns with 12 loaves of bread.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Real programmers count from 0.",
    "What is the most used language in programming? Profanity.",
    "I'd tell you a joke about UDP, but you might not get it.",
    "A SQL query walks into a bar and sees two tables. He walks up to them and says, 'Can I join you?'"
]
FACTS = [
    "Honey never spoils. Archaeologists have found 3000-year-old honey still edible.",
    "A group of flamingos is called a flamboyance.",
    "The Eiffel Tower can be 15 centimetres taller in summer due to thermal expansion.",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are technically berries, but strawberries are not.",
    "The shortest war in history lasted 38 to 45 minutes.",
    "Cleopatra lived closer in time to the Moon landing than to the building of the pyramids.",
    "There are more possible chess games than atoms in the observable universe.",
    "The human brain uses approximately 20 watts of power.",
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

def tell_fact() -> str:
    fact=random.choice(FACTS)
    logger.info("Fact told")
    return f"Here is an intresting fact {fact}"

def flip_coin() -> str:
    result=random.choice(["heads","tails"])
    logger.info(f"Flipped coin : {result}")
    return f"I Flipped the coin and got {result}"

def roll_dice() -> str:
    result=random.randint(1,6)
    logger.info(f"Dice roll : {result}")
    return f"I rolled the dice and got {result}"


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
    logger.info("google calendar opened.")
    return "opening your google calendar. "


#Volume and system controls
def take_screenshots()-> str:
    try:
        import datetime
        timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        desktop=os.path.join(os.path.expanduser("~"),"Desktop")
        filepath=os.path.join(desktop,f"automoto_screenshot_{timestamp}.png")

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
    if not command or not command.strip():
        return "I didn't hear anything. Please say something."
    
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
    
    if any(w in command for w in ["calendar","open calendar", "schedule", "my schedule"]):
        return open_calendar()

    if any(w in command for w in ["system information","system info"]):
        return get_system_info()

    if any(w in command for w in ["flip a coin", "flip coin", "coin flip", "toss a coin"]):
        return flip_coin()

    if any(w in command for w in ["roll a dice", "roll dice", "roll the dice", "dice"]):
        return roll_dice()

    if any(w in command for w in ["fact", "tell me a fact", "interesting fact", "something interesting"]):
        return tell_fact()

    if any(w in command for w in ["screenshot","take a screenshot"]):
        return take_screenshots()

    if any(w in command for w in ["joke","make me laugh","funny"]):
        return tell_joke()

    if any(w in command for w in ["help","what can you do","commands"]):
        return get_help()

    if any(ext in command for ext in ["goodbye", "exit", "stop", "quit", "bye"]):
        return "EXIT: Shutting down. Goodbye!"
        
    small_talk=get_small_talk_response(command)
    if small_talk:
        return small_talk

    logger.warning(f"Unknown command : '{command}")
    return(
        f"I am not sure how to handle that."
        f"say help to hear what i can do."
    )