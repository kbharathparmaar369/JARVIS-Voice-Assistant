import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.commands import process_command
from module1.speech import speak

print("="*50)
print("AutoMoto Day 3 - COMMAND PROCESSOR TEST")
print("="*50)

tests=[
    ("what time is it" , "Time query"),
    ("what is today's date", "Date query"),
    ("search wikipedia python programming", "Wikipedia search"),
    ("search wikipedia Maharana pratap",          "Wikipedia disambiguation"),
    ("search google best python projects",  "Google search"),
    ("open youtube lofi music",             "YouTube with query"),
    ("tell me a joke",                      "Joke"),
    ("how are you",                         "Small talk - how are you"),
    ("who are you",                         "Small talk - identity"),
    ("who made you",                        "Small talk - creator"),
    ("what can you do",                     "Help / commands list"),
    ("help",                                "Help trigger"),
    ("thank you",                           "Small talk - thanks"),
    ("open calculator",                     "Unknown → fallback"),
    ("goodbye",                             "Exit signal"),
]

passed=0
failed=0

for command , description in tests:
    print(f"\n{'-'*50}")
    print(f"TEST : {description}")
    print(f"Input:'{command}'")

    result=process_command(command)
    print(f"OUTPUT : '{result[:80]} {'...' if len(result) > 80 else ''}'")

    if result:
        print("Status : PASSED")
        passed+=1
    else:
        print("Status : FAILED - EMPTY RESPONSE")
        failed+=1

print(f"\n{'='*50}")
print(f"Results : {passed} passed , {failed} failed out of {len(tests)} tests")
print(f"{'='*50}\n")

print("Now speaking some responses aloud... \n")
speak(process_command("what time is it"))
speak(process_command("what is today's date"))
speak(process_command("tell me a joke"))
speak("Day 3 testing compelete. Command processor is fully operational")