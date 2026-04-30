import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.commands import process_command
from module1.speech import speak

print("="*50)
print("AutoMoto DAY 5  TEST")
print("="*50)

tests = [
    # Identity
    ("who are you",               "Identity"),
    ("who made you",              "Creator"),
    ("are you human",             "Human check"),
    ("are you alive",             "Philosophical"),
    ("what is your purpose",      "Purpose"),
    ("do you have feelings",      "Feelings"),
    ("do you sleep",              "Sleep"),

    # Greetings
    ("hello",                     "Hello greeting"),
    ("good morning",              "Morning greeting"),
    ("good night",                "Night greeting"),

    # Appreciation
    ("thank you",                 "Thank you"),
    ("you're awesome",            "Compliment"),
    ("you are stupid",            "Insult handling"),
    ("i hate you",                "Hate handling"),
    ("shut up",                   "Shut up handling"),

    # Fun
    ("tell me a joke",            "Joke"),
    ("tell me a fact",            "Fact"),
    ("flip a coin",               "Coin flip"),
    ("roll a dice",               "Dice roll"),
    ("tell me a story",           "Story"),
    ("sing a song",               "Sing"),
    ("what is the meaning of life", "Deep question"),
    ("are you better than siri",  "Competitor comparison"),

    # Help
    ("help",                      "Help command"),

    # Regression checks
    ("what time is it",           "Time — regression"),
    ("open calculator",           "Calculator — regression"),
    ("goodbye",                   "Exit signal"),
]

passed=0
failed=0

for command, description in tests:
    print(f"\n{'-'*50}")
    print(f"Test : {description}")
    print(f"Input : '{command}'")

    result=process_command(command)
    display=result[:80] + ("..." if len(result) > 80 else "")
    print(f"OUTPUT : '{display}'")

    if result:
        print("status : PASSED")
        passed+=1
    else:
        print("Status : Failed")
        failed+=1
        
print(f"RESULTS :{passed} passed , {failed} out of {len(tests)} tests")
print(f"{'='*50}")

print("Speaking personality rspnoses aloud :.. \n")
speak(process_command("who are you "))
speak(process_command("tell me a joke"))
speak(process_command("tell me a fact"))
speak(process_command("flip a coin"))
speak(process_command("roll a dice"))
speak(process_command("what is the meaning of life"))
speak("Day 5 personality testing complete. AutoMoto is fully alive.")