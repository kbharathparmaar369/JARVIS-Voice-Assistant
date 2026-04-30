from collections import deque
from datetime import datetime
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from module1.config import MAX_HISTORY

class CommandHistory:
    #track recent voice commands and response in memory

    def __init__(self,max_size: int=MAX_HISTORY):
        self._history=deque(maxlen=max_size)
        self.total_commands=0

    def add(self, command: str,response: str)-> None:
        entry={
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "command"  : command,
            "response" : response[:100], #truncate the long responses
        }
        self._history.append(entry)
        self.total_commands+=1

    def get_last(self, n: int=3) -> list:
        entries=list(self._history)
        return entries[-n:] if n <= len(entries) else entries

    def get_all(self) -> list:
        return list(self._history)
    
    def clear(self) -> None:
        self._history.clear()
    
    def summary(self) -> str:
        if not self._history:
            return "you have not given me any commands yet"

        recent=self.get_last(3)
        lines=[f"you said : {e['command']} "for e in recent]
        return( 
            f"In this session you have given me"
            f"{self.total_commands} commands"
            f"your last{len(recent)} were :"
            +",then ".join(lines) + "."
        )

    def __len__(self)-> int:
        return len(self._history)

command_history=CommandHistory()