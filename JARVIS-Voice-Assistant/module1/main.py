from module1.logger import log_command
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from module1.speech import speak, listen , greet_user
from module1.commands import process_command
from module1.config   import ASSISTANT_NAME
from module1.logger import setup_logger,log_session_start,log_session_end,log_command
from module1.history import command_history

logger=setup_logger("main")

banner=f"""

|-------------------------------------------------------|
| {ASSISTANT_NAME.upper()}- PERSONAL AI VOICE ASSISTANT |                                              
|                      MODULE 1 -CLI                    |  
|=======================================================|
|   Say 'help'     -> hear all available commands        |                                      
|   Say 'history'  -> hear your recent commands          |
|   Say 'goodbye'  -> shut down AutoMoto                 |                                  
|-------------------------------------------------------| 
"""

print(banner)


def run_automoto ()-> None:
    print(banner)
    log_session_start()
    logger.info("AutoMoto session started..")

    greet_user()

    while True:
        try:
            command=listen()

            if not command:
                continue

            #History command not in command.py
            if any(w in command for w in ["history","what did i say","recent commands"]):
                response=command_history.summary()
                speak(response)
                command_history.add(command, response)
                log_command(command, response)
                continue
            
            response=process_command(command)

            if "EXIT" in response:
                farewell=(
                    f"Goodbye. It was a pleasure assisting you. "
                    f"This session had {command_history.total_commands} commands. "
                    f"Shutting down now."
                )
                speak(farewell)
                log_command(command,"EXIT")
                logger.info("AutoMoto shutdown by user")
                log_session_end()
                break
            if response:
                speak(response)
                command_history.add(command,response)
                log_command(command,response)

        except KeyboardInterrupt:
            print("\n\n  [SYSTEM] Ctrl+C detected — shutting down.")
            speak("Shutting down. Goodbye.")
            logger.info("AutoMoto shutdown via KeyboardInterrupt.")
            log_session_end()
            break

        except Exception as e:
            logger.info(f"Main Loop error : {e} ")
            speak("I encounterd an unexpected error . Resumimg. ")
            continue

if __name__ == "__main__":
    run_automoto()
