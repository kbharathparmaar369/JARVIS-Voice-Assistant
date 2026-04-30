from test_day3 import passed
from sre_constants import SUCCESS
from test_day2 import result
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.speech import speak , greet_user
from module1.commands import process_command
from module1.logger import setup_logger,log_session_start,log_session_end
from module1.history import CommandHistory

logger=setup_logger("final test")

class TestRunner:
    def __init__(self):
        self.passed=0
        self.failed=0
        self.results=[]

    def run(self,description: str,command: str,must_contain: str="") -> bool:
        result=process_command(command.lower().strip())
        success=bool(result)

        if must_contain and success:
            success=must_contain.lower() in result.lower()

        status="PASS" if success else "FAIL"
        output=result[:60] +"..." if len(result) > 60 else result

        print(f"{status} | {description}")
        print(f"Input :'{command}'")
        print(f"Output : '{output}'")

        if success:
            self.passed+=1
        else:
            self.failed+=1
        
        self.results.append({
            "desc" : description,
            "command": command,
            "result": result,
            "passed" : success
        })
        return success

    def section(self,title: str) -> None:
        print(f"\n {'-'*50}")
        print(f"SECTION: {title}")
        print(f"{'-'*50}")

    def summary(self) -> None:
        total=self.passed + self.failed
        pct=int((self.passed/total)*100) if total > 0 else 0
        print(f"\n {'-'*50}")
        print("Final Results")
        print(f"Final Results")
        print(f"Passed : {self.passed}/{total}")
        print(f"Failed : {self.failed}/{total}")
        print(f"Score : {pct}%")

        if self.failed ==0:
            print(f"\n ALL TEST PASSED - Module 1 is demo ready !")
        
        else:
            print(f"\n {self.failed} test failed - fix before recording demo")
            print("\n Failed tests :")
            for r in self.results:
                if not r["passed"]:
                    print(f"-> '{r['command']}'")
        
        print(f"{'='*50}\n ")


def run_full_test():
    print("\n" + "="*55)
    print("  AutoMoto MODULE 1 — FINAL TEST SUITE")
    print("="*55)

    t = TestRunner()
    log_session_start()

    # ─────────────────────────────────────────────────────
    t.section("1. TIME & DATE")
    t.run("Time query",             "what time is it",       "it is")
    t.run("Time alternate phrasing","tell me the time",      "it is")
    t.run("Date query",             "what is today's date",  "today is")
    t.run("Day query",              "what day is it",        "today is")

    # ─────────────────────────────────────────────────────
    t.section("2. WIKIPEDIA")
    t.run("Wikipedia — clear query",      "search wikipedia python", "wikipedia")
    t.run("Wikipedia — multi word",       "search wikipedia artificial intelligence", "wikipedia")
    t.run("Wikipedia — no query",         "wikipedia",               "would you like")
    t.run("Wikipedia — named person",     "search wikipedia albert einstein", "wikipedia")

    # ─────────────────────────────────────────────────────
    t.section("3. WEB BROWSER")
    t.run("Google search",         "search google python tutorials",  "opening google")
    t.run("Google alternate",      "search for best python projects", "opening google")
    t.run("YouTube with query",    "open youtube lofi music",         "youtube")
    t.run("YouTube no query",      "youtube",                         "youtube")

    # ─────────────────────────────────────────────────────
    t.section("4. SYSTEM APPS")
    t.run("Calculator",            "open calculator",    "calculator")
    t.run("Notepad",               "open notepad",       "notepad")
    t.run("CMD",                   "open command prompt","cmd")
    t.run("Paint",                 "open paint",         "paint")
    t.run("File Explorer",         "open file explorer", "explorer")

    # ─────────────────────────────────────────────────────
    t.section("5. MUSIC & CALENDAR")
    t.run("Play music",            "play music",         "music")
    t.run("Play song",             "play a song",        "music")
    t.run("Calendar",              "open calendar",      "calendar")
    t.run("Schedule",              "my schedule",        "calendar")

    # ─────────────────────────────────────────────────────
    t.section("6. SYSTEM UTILITIES")
    t.run("System info",           "system info",        "running")
    t.run("Screenshot",            "take screenshot",    "screenshot")

    # ─────────────────────────────────────────────────────
    t.section("7. PERSONALITY — IDENTITY")
    t.run("Who are you",           "who are you",        "automoto")
    t.run("Who made you",          "who made you",       "built")
    t.run("Are you human",         "are you human",      "artificial")
    t.run("Are you alive",         "are you alive",      "philosophical")
    t.run("What is your purpose",  "what is your purpose","assist")
    t.run("Do you sleep",          "do you sleep",       "not sleep")
    t.run("Your name",             "what's your name",   "automoto")

    # ─────────────────────────────────────────────────────
    t.section("8. PERSONALITY — GREETINGS")
    t.run("Hello",                 "hello",              "hello")
    t.run("Good morning",          "good morning",       "morning")
    t.run("Good night",            "good night",         "night")
    t.run("Thank you",             "thank you",          "welcome")
    t.run("Compliment",            "you're awesome",     "appreciate")
    t.run("Insult handling",       "you are stupid",     "sorry")
    t.run("Shut up",               "shut up",            "quiet")

    # ─────────────────────────────────────────────────────
    t.section("9. FUN & GAMES")
    t.run("Joke",                  "tell me a joke",     "")
    t.run("Fact",                  "tell me a fact",     "fact")
    t.run("Coin flip",             "flip a coin",        "coin")
    t.run("Dice roll",             "roll a dice",        "dice")
    t.run("Story",                 "tell me a story",    "once")
    t.run("Meaning of life",       "what is the meaning of life", "42")

    # ─────────────────────────────────────────────────────
    t.section("10. EDGE CASES")
    t.run("Empty input",           "",                   "")
    t.run("Unknown command",       "xyzzy banana tree",  "not sure")
    t.run("Help command",          "help",               "can do")
    t.run("Exit signal",           "goodbye",            "EXIT")

    t.section("11. COMMAND HISTORY")
    history = CommandHistory()
    for r in t.results[:5]:
        history.add(r["command"], r["result"])

    summary = history.summary()
    has_summary = "commands" in summary.lower()
    print(f"  {'OK PASS' if has_summary else 'FAIL FAIL'} | History summary generated")
    print(f"         Output: '{summary[:60]}...'")
    if has_summary:
        t.passed += 1
    else:
        t.failed += 1

    # -----------------------------------------------------
    t.section("12. LOG FILES")
    log_session_end()
    for log_file in ["logs/automoto.log", "logs/errors.log", "logs/session.log"]:
        exists = os.path.exists(log_file)
        size   = os.path.getsize(log_file) if exists else 0
        print(f"  {'OK PASS' if exists else 'FAIL FAIL'} | {log_file} "
              f"({'exists, ' + str(size) + ' bytes' if exists else 'MISSING'})")
        if exists:
            t.passed += 1
        else:
            t.failed += 1

    # ─────────────────────────────────────────────────────
    t.summary()

    # Speak the final result
    if t.failed == 0:
        speak(
            f"All tests passed. "
            f"Module 1 is complete and ready for demonstration. "
            f"Excellent work."
        )
    else:
        speak(
            f"{t.failed} tests failed. "
            f"Please review the terminal output and fix the issues."
        )


if __name__ == "__main__":
    run_full_test()
