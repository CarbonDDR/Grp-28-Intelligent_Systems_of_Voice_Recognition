"""
Developer   : Naman Dave
College ID  : 201801439
About       : Voice Assistant functionalities
Sources     :
Voice Assistant: https://www.geeksforgeeks.org/voice-assistant-using-python/
"""


import shutil
import pyttsx3
import smtplib
import datetime
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

try:
    engine.setProperty("voice", voices[1].id)
except:
    engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def ask():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return ""

    return query
