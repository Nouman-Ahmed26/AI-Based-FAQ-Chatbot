import pyttsx3
import pywhatkit
import random
import platform

# Choose the best driver explicitly for stability
def _default_driver():
    sysname = platform.system().lower()
    if sysname == "windows":
        return "sapi5"
    if sysname == "darwin":
        return "nsss"
    return "espeak"

def _make_engine():
    eng = pyttsx3.init(_default_driver())
    eng.setProperty('rate', 150)
    eng.setProperty('volume', 1.0)
    return eng

def talk(text):
    """Print and speak one utterance reliably."""
    print(f"Dobby: {text}")
    tts = _make_engine()
    tts.say(text)
    tts.runAndWait()
    tts.stop()

def get_response(command):
    """Generates replies for text input only."""
    command = command.lower().strip()

    # --- Greetings ---
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    if command in greetings:
        responses = [
            "Hello there! How are you today?",
            "Hey! Nice to see you again.",
            "Hi! Hope you're doing great!",
            "Hello! Ready to chat?",
            "Hey friend! What’s up?"
        ]
        talk(random.choice(responses))
        return

    # --- Play song ---
    if command.startswith("play "):
        song = command.replace("play", "").strip()
        if song:
            reply = f"Playing {song} on YouTube."
            talk(reply)
            try:
                pywhatkit.playonyt(song)
            except Exception:
                talk("Sorry, I couldn't open YouTube right now.")
        else:
            talk("Please specify the song name after 'play'.")
        return

    # --- Search online ---
    if command.startswith("search for "):
        query = command.replace("search for", "").strip()
        if query:
            reply = f"Searching for {query}."
            talk(reply)
            try:
                pywhatkit.search(query)
            except Exception:
                talk("Sorry, I couldn't open the browser for that search.")
        else:
            talk("Please specify what to search for.")
        return

    # --- FAQ responses ---
    if "who are you" in command or "your name" in command:
        talk("I’m Dobby, your friendly text and voice assistant.")
    elif "how are you" in command:
        talk("I’m doing great, thanks for asking! How about you?")
    elif "what can you do" in command:
        talk("I can play songs, search the web, and chat with you.")
    elif "who created you" in command:
        talk("I was created by Mohammed Nouman Ahmed.")
    elif "thank you" in command or "thanks" in command:
        talk(random.choice(["You're welcome!", "Glad to help!", "Anytime!"]))
    elif "bye" in command or "exit" in command or "stop" in command:
        talk(random.choice(["Goodbye!", "See you later!", "Bye! Have a great day!"]))
        return "exit"
    else:
        talk(random.choice([
            "I’m not sure about that, but I’ll learn soon!",
            "Hmm, that’s interesting.",
            "Sorry, I didn’t quite get that.",
            "Could you say that another way?"
        ]))

def run_assistant():
    """Main chatbot loop — text only."""
    talk(random.choice([
        "Hello! I’m Dobby, your assistant. How can I help you today?",
        "Hi! Dobby here, ready to chat!",
        "Hey there! What would you like me to do?"
    ]))

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        result = get_response(user_input)
        if result == "exit":
            break

if __name__ == "__main__":
    run_assistant()
