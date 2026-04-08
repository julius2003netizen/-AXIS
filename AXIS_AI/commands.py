import os
from voice import speak

def run(command):

    if "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")
        return True

    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
        return True

    return False
