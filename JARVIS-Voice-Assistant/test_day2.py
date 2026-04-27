import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.speech import speak, listen, greet_user

print("="*50)
print("AutoMoto day 2 test")
print("="*50)

#test 1 basic tts
print("\n [Test 2] tts edge cases...")
speak("")
speak(" ")
speak("Testing numbers : 1,2,3.")

#boot greeting
print("\n [TEST 3] Boot greeting ...")
greet_user()

#Listen once

print("\n [TEST 4] microphone listen test ..")
speak("I am ready to listen . Please say a command after the prompt.")
result=listen()

if result:
    speak(f"I heard you say : {result}")
    print(f"\n listen () returned : '{result}'")
else:
    print("\n listen() empty - check mic or speak louder")

print("\n [TEST 5] Listen loop - say 3  different things...")
speak("Now i will listen 3 times in a row . Say something each time")

for i in range(1,4):
    speak(f"Command {i} , go ahead.")
    command=listen()

    if command:
        speak(f"Got it . you said : {command}")
    else:
        speak("I missed that one .")
speak("Day 2 Testing complete . All system verified..")
print("="*50)
print("Day 2 test complete")
print("="*50)