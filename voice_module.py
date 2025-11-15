import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to audio and convert to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network.")
        return ""
