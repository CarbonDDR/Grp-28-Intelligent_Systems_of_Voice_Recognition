import psutil
import os
import webbrowser
import random
import string
from sys import platform
import psutil as p
from src.va import speak,ask
import datetime
import subprocess
import screen_brightness_control as sbc
import requests
import json
import wolframalpha



def mozila():
    if platform == "linux" or platform == "linux2":
        subprocess.run('firefox',shell=True)
    elif platform == "darwin":
        subprocess.run('open -a Firefox --args -private-window',shell=True)
    elif platform == "win32":
        subprocess.run('start firefox',shell=True)
    else:
        speak("Unsupported OS")

def mozila_caller(input_string):
    mozila()



def tell_time():
    tim=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Sir, The time is: ")
    speak(tim)

def tell_time_caller(input_string):
    tell_time()




def gk(query):
    app_id="A5JYYE-TPRTRVW2AX"
    cilent=wolframalpha.Client(app_id)
    ind=query.split().index("is")
    text=query.split()[ind+1:]
    res=cilent.query(" ".join(text))
    answer=next(res.results).text
    ans=""
    for i in text:
        ans+=i
        ans+=" "
    ans=ans+"is "+answer
    print(ans)
    speak(ans)

def gk_caller(input_string):
    gk(input_string)




def brightness(query):
    res = [int(i) for i in query.split() if i.isdigit()]
    if len(res)==0:
        speak("No digit specified")
    else:
        lev=res[0]
        current_brightness=sbc.get_brightness()
        new_lev=lev
        if "increment" in query or "add" in query or "increase" in query or "up" in query or "high" in query:
            new_lev=min(current_brightness+lev,100)
            sbc.set_brightness(new_lev)
            
        elif "decrement" in query or "subtract" in query or "decrease" in query or "low" in query or "down" in query:
            new_lev=max(lev-current_brightness,0)
            sbc.set_brightness(new_lev)
        else:
            if new_lev>100:
                new_lev=100
            elif new_lev<0:
                new_lev=0
            sbc.set_brightness(new_lev)
        speak("Brightness is changed to"+ str(new_lev))

def brightness_caller(input_string):
    brightness(input_string)




def google_map(query):
    ind=query.split().index("is")
    location=query.split()[ind+1:]
    url="https://www.google.com/maps/place/"+"".join(location)
    speak("This is where"+str(location)+"is.")
    webbrowser.open_new_tab(url)

def google_map_caller(input_string):
    google_map(input_string)


def weather(query):
    key = "772992eec7a54fc87f19fcf6fc03d643"
    weather_url="http://api.openweathermap.org/data/2.5/weather?"
    ind=query.split().index("in")
    location=query.split()[ind+1:]
    location="".join(location)
    url=weather_url+"appid="+key+"&q="+location
    js=requests.get(url).json()
    if js["cod"] != "404":
        temp= js["main"]
        tem=temp["temp"]
        tem=tem-273.15
        humidity=temp["humidity"]
        desc=js["weather"][0]["description"]
        response="The temperature in Calcius is"+str(tem) +" The humidity is"+str(humidity)+" and the weather description is"+str(desc)
        speak(response)
    else:
        speak("City not found")

def weather_caller(input_string):
    weather(input_string)


# def screenshot():
#     img=pyautogui.screenshot()

#     img.save(".\screenshot\screenshot1.png")
#     speak("Screenshot is taken. To see your screenshot open screenshot folder in current directory")

def news():
    url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=e19bfb969c6840549b0244cca9f1fb83')
    try:
        response=requests.get(url)
    except:
        speak("Please Check your connection")
    
    news=json.loads(response.text)
    k=1
    for new in news["articles"]:
        k+=1
        print(str(new["title"]),"\n")
        speak(str(new["title"]))
        print(str(new["description"]),"\n")
        speak(str(new["description"]))
        if k==6:
            break
    response = requests.get(url)

def news_caller(input_string):
    news()


hash_dict={
                "open mozila":mozila_caller,"open firefox":mozila_caller,"open mozila firefox":mozila_caller,
                "start mozila":mozila_caller,"start firefox":mozila_caller,"start mozila firefox":mozila_caller,
                "tell time":tell_time_caller,"what is the time":tell_time_caller,
                "who is":gk_caller,"what is":gk_caller,
                "incremet brightness":brightness_caller,"add brightness":brightness_caller,
                "increase brightness":brightness_caller,"up brightness":brightness_caller,
                "high brightness":brightness_caller,
                "decrement brightness":brightness_caller,"subtract brightness":brightness_caller,
                "decrease brightness":brightness_caller,"low brightness":brightness_caller,
                "down brightness":brightness_caller,"set brightness":brightness_caller,
                "weather":weather_caller,
                "news":news_caller
}
