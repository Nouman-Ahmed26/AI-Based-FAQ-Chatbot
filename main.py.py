import tkinter as tk
import pyttsx3
import pywhatkit
import random
import platform

# Pick best driver for TTS engine
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
    print(f"Dobby: {text}")
    tts = _make_engine()
    tts.say(text)
    tts.runAndWait()
    tts.stop()

faq = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm an AI assistant. I'm always ready to help.",
    "what's your name": "I'm Dobby, your voice assistant.",
    "bye": "Goodbye! Have a nice day.",
    "who made you": "I was created by Mohammed Nouman Ahmed.",
    "what can you do": "I can answer questions and play songs for you. Try asking for a song!",
    "tell me a joke": "Why did the AI stay home from work? It had a byte fever!",
    "who am i": "You are an awesome user talking to me right now.",
    "what is your age": "I don't age."
}

def handle_query(query):
    query = query.lower().strip()
    answer = "Sorry, I don't know that. Try another one!"
    if query.startswith("play "):
        song = query.replace("play ", "", 1).strip()
        answer = f"Playing {song} on YouTube!"
        talk(answer)
        try:
            pywhatkit.playonyt(song)
        except Exception:
            talk("Sorry, I couldn't open YouTube right now.")
    elif query.startswith("search for "):
        search_term = query.replace("search for ", "", 1).strip()
        answer = f"Searching for {search_term}."
        talk(answer)
        try:
            pywhatkit.search(search_term)
        except Exception:
            talk("Sorry, I couldn't open the browser for that search.")
    elif query in faq:
        answer = faq[query]
        talk(answer)
    else:
        talk(answer)
    answer_text.delete('1.0', tk.END)
    answer_text.insert(tk.END, answer)

def submit():
    query = question_entry.get()
    handle_query(query)

root = tk.Tk()
root.title("Dobby Assistant")
root.geometry("500x340")

tk.Label(root, text="Ask a question or type 'play ...' or 'search for ...'").pack(pady=8)
question_entry = tk.Entry(root, width=50)
question_entry.pack()

# ONLY the Send button
tk.Button(root, text="Send", command=submit).pack(pady=6)

answer_text = tk.Text(root, height=6, width=60)
answer_text.pack(pady=8)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
