import psutil
import pyttsx3
import warnings
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import random
import subprocess
import string
import time
from sys import platform
import psutil as p
import datetime
from src.va import speak, ask

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)


def open_chrome():

    if platform == "linux" or platform == "linux2":
        subprocess.run("chrome", shell=True)
    elif platform == "darwin":
        subprocess.run("open -a Chrome --args -private-window", shell=True)
    elif platform == "win32":
        subprocess.run("start chrome", shell=True)
    else:
        speak("Unsupported OS")

    # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    # webbrowser.get('chrome').open_new_tab('https://google.com')


def chrome_caller(input_string):
    open_chrome()


def main_date():

    now = datetime.datetime.now()
    speak("Sir, the Current Date is : " + now.strftime("%m-%d-%Y") + "\n")
    print("Sir, the Current Date is : ")
    print(now.strftime("%d-%m-%Y") + "\n")
    print("")


def date_caller(input_string):
    main_date()


def search_wiki():
    speak("What do you want to search on wikipedia ?")
    sinwiki = ask()
    sinwiki = sinwiki.replace("wikipedia", "")
    results = wikipedia.summary(sinwiki, sentences=2)
    print(results)
    speak("According to Wikipedia,")
    speak(results)


def search_wiki_caller(input_string):
    search_wiki()


hash_201801012 = {
    "Open Chrome": chrome_caller,
    "open chrome": chrome_caller,
    "start chrome": chrome_caller,
    "begin chrome": chrome_caller,
    "begin the chrome": chrome_caller,
    "initiate chrome": chrome_caller,
    "open chrome": chrome_caller,
    "start chrome": chrome_caller,
    "what is date": date_caller,
    "show the date": date_caller,
    "show date": date_caller,
    "display the date": date_caller,
    "display date": date_caller,
    "say date": date_caller,
    "search on wiki": search_wiki_caller,
    "search on wikipedia": search_wiki_caller,
}
