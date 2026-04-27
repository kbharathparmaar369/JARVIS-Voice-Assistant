from os.path import abspath
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.commands import process_command
from module1.speech import speak

print("="*50)
print("AutoMoto DAY 4 SYSTEM INTEGRATION TEST")
print("="*50)

tests=[
    # System apps
    ("open calculator",        "Open Calculator"),
    ("open notepad",           "Open Notepad"),
    ("open command prompt",    "Open CMD"),
    ("open paint",             "Open Paint"),
    ("open file explorer",     "Open File Explorer"),

    # Music
    ("play music",             "Play Music"),

    # Calendar
    ("open calendar",          "Open Calendar"),

    # System info
    ("system info",            "System Info"),

    # Screenshot
    ("take screenshot",        "Screenshot"),

    # All previous Day 3 still working
    ("what time is it",        "Time — regression check"),
    ("tell me a joke",         "Joke — regression check"),
    ("search wikipedia india", "Wikipedia — regression check"),
    ("goodbye",                "Exit signal"),
]

passed=0
failed=0
for command , description in tests:
    print(f"\n{'-'*50}")
    print(f"TEST : {description}")
    print(f"INPUT : '{command}'")

    result =process_command(command)
    display=result[:60] + ("..." if len(result) > 80 else "")
    print(f"OUTPUT : '{display}'")

    if result:
        print("STATUS : PASS")
        passed += 1
    else:
        print("STATUS : FAIL - empty response")
        failed+=1

print(f"\n{'='*50}")
print(f"RESULTS : {passed} passed , {failed} failed out of {len(tests)} tests")
print(f"{'='*50}\n")

#speak key results

print("Speaking key results aloud ... \n")
speak(process_command("open calculator"))
speak(process_command("system info"))
speak(process_command("play music"))
speak("Day 4 system integration testing compelete")

