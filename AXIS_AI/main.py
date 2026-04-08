from listener import listen
from voice import speak
from brain import ask_axis
from commands import run
from config import WAKE_WORD

speak("AXIS online.")

while True:

    command = listen().lower()
    print("You:", command)

    if not command.startswith(WAKE_WORD):
        continue

    command = command.replace(WAKE_WORD, "").strip()

    if "shutdown" in command:
        speak("Shutting down. Goodbye.")
        break

    if run(command):
        continue

    reply = ask_axis(command)
    speak(reply)
