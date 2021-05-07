import psutil
import os
import webbrowser
import random
import string
from sys import platform
import psutil as p
from src.va import speak, ask
import datetime
import subprocess
import screen_brightness_control as sbc
import requests
import json
import wolframalpha

# * New modules to impoer
from bs4 import BeautifulSoup
import re

# * open mozila in linux,windows and mac os
def mozila():
    if platform == "linux" or platform == "linux2":
        subprocess.run("firefox", shell=True)
    elif platform == "darwin":
        subprocess.run("open -a Firefox --args -private-window", shell=True)
    elif platform == "win32":
        subprocess.run("start firefox", shell=True)
    else:
        speak("Unsupported OS")


def mozila_caller(input_string):
    mozila()


# * tell the current time
def tell_time():
    tim = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Sir, The time is: ")
    print(tim)
    speak(tim)


def tell_time_caller(input_string):
    tell_time()


# * Answer the questions that are starting from what and who
def gk(query):
    app_id = "A5JYYE-TPRTRVW2AX"
    cilent = wolframalpha.Client(app_id)
    ind = query.split().index("is")
    text = query.split()[ind + 1 :]
    res = cilent.query(" ".join(text))
    answer = next(res.results).text
    ans = ""
    for i in text:
        ans += i
        ans += " "
    ans = ans + "is " + answer
    print(ans)
    speak(ans)


def gk_caller(input_string):
    gk(input_string)


# * Set the brightness of your device
def brightness(query):
    res = [int(i) for i in query.split() if i.isdigit()]
    if len(res) == 0:
        speak("No digit specified")
    else:
        lev = res[0]
        current_brightness = sbc.get_brightness()
        new_lev = lev
        if (
            "increment" in query
            or "add" in query
            or "increase" in query
            or "up" in query
            or "high" in query
        ):
            new_lev = min(current_brightness + lev, 100)
            sbc.set_brightness(new_lev)

        elif (
            "decrement" in query
            or "subtract" in query
            or "decrease" in query
            or "low" in query
            or "down" in query
        ):
            print(lev)
            new_lev = max(current_brightness - lev, 0)
            sbc.set_brightness(new_lev)
        else:
            if new_lev > 100:
                new_lev = 100
            elif new_lev < 0:
                new_lev = 0
            sbc.set_brightness(new_lev)
        speak("Brightness is changed to" + str(new_lev))


def brightness_caller(input_string):
    brightness(input_string)


# * Show you the location in google map
def google_map(query):
    ind = query.split().index("is")
    location = query.split()[ind + 1 :]
    url = "https://www.google.com/maps/place/" + " ".join(location)
    speak("This is where" + str(location) + "is.")
    webbrowser.open_new_tab(url)


def google_map_caller(input_string):
    google_map(input_string)


# * tell you the weather
def weather(query):
    key = "772992eec7a54fc87f19fcf6fc03d643"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    if "in" in query:
        ind = query.split().index("in")
    else:
        ind = query.split().index("of")
    # print(ind)
    location = query.split()[ind + 1 :]
    location = "".join(location)
    url = weather_url + "appid=" + key + "&q=" + location
    js = requests.get(url).json()
    if js["cod"] != "404":
        temp = js["main"]
        tem = temp["temp"]
        tem = tem - 273.15
        humidity = temp["humidity"]
        desc = js["weather"][0]["description"]
        response = (
            "The temperature in Calcius is "
            + str(round(tem, 2))
            + " The humidity is "
            + str(round(humidity, 2))
            + " and the weather description is "
            + str(desc)
        )
        print(response)
        speak(response)
    else:
        speak("City not found")


def weather_caller(input_string):
    weather(input_string)


# * tell you the 10 headlines of India
def news():
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=e19bfb969c6840549b0244cca9f1fb83"
    try:
        response = requests.get(url)
    except:
        speak("Please Check your connection")

    news = json.loads(response.text)
    k = 1
    for new in news["articles"]:
        k += 1
        print(str(new["title"]), "\n")
        speak(str(new["title"]))
        print(str(new["description"]), "\n")
        speak(str(new["description"]))
        if k >= 3:
            break
    response = requests.get(url)


def news_caller(input_string):
    news()


# *show the stats of corona in India
def corona():
    url = "https://www.worldometers.info/coronavirus/country/india/"  # Website URL address used for web-scraping
    req = requests.get(url)
    bsObj = BeautifulSoup(req.text, "html.parser")
    data = bsObj.find_all("div", class_="maincounter-number")
    print("Collecting the data....")
    speak("Collecting the data")
    print("Total Cases: ", data[0].text.strip())
    speak("Total Cases: " + data[0].text.strip())
    print("Total Deaths: ", data[1].text.strip())
    speak("Total Deaths: " + data[1].text.strip())
    print("Total Recovered: ", data[2].text.strip())
    speak("Total Recovered: " + data[2].text.strip())


def corona_caller(input_string):
    corona()


# * Suggest you the books that are top read for week
def book_suggest():
    url = "https://www.goodreads.com/book/most_read"  # Website URL address used for web-scraping
    req = requests.get(url)
    bsObj = BeautifulSoup(req.text, "html.parser")
    book_title = bsObj.find_all(class_="bookTitle")
    author_name = bsObj.find_all(class_="authorName")

    print("Here are the 5 Most Read Books This Week \n")
    speak("Here are the 5 Most Read Books This Week")
    print(book_title[0].text.strip() + " by " + author_name[0].text.strip())
    speak(book_title[0].text.strip() + " by " + author_name[0].text.strip())
    print(book_title[1].text.strip() + " by " + author_name[1].text.strip())
    speak(book_title[1].text.strip() + " by " + author_name[1].text.strip())
    print(book_title[2].text.strip() + " by " + author_name[2].text.strip())
    speak(book_title[2].text.strip() + " by " + author_name[2].text.strip())
    print(book_title[3].text.strip() + " by " + author_name[3].text.strip())
    speak(book_title[3].text.strip() + " by " + author_name[3].text.strip())
    print(book_title[4].text.strip() + " by " + author_name[4].text.strip())
    speak(book_title[4].text.strip() + " by " + author_name[4].text.strip())


def book_suggest_caller(input_string):
    book_suggest()


# * suggest movie or show the top 10 imdb rated movie
def movie_suggest():
    url = "http://www.imdb.com/chart/top"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.select("td.titleColumn")
    links = [a.attrs.get("href") for a in soup.select("td.titleColumn a")]
    crew = [a.attrs.get("title") for a in soup.select("td.titleColumn a")]
    ratings = [
        b.attrs.get("data-value") for b in soup.select("td.posterColumn span[name=ir]")
    ]
    votes = [b.attrs.get("data-value") for b in soup.select("td.ratingColumn strong")]

    imdb = []

    # Store each item into dictionary (data), then put those into a list (imdb)
    for index in range(0, len(movies)):
        # Seperate movie into: 'place', 'title', 'year'
        movie_string = movies[index].get_text()
        movie = " ".join(movie_string.split()).replace(".", "")
        movie_title = movie[len(str(index)) + 1 : -7]
        year = re.search("\((.*?)\)", movie_string).group(1)
        place = movie[: len(str(index)) - (len(movie))]
        data = {
            "movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index],
        }
        imdb.append(data)
    speak("Here is the top 10 imdb rating movie to watch.")
    k = 0
    for item in imdb:
        print(k + 1, "-", item["movie_title"])
        speak(item["movie_title"])
        k += 1
        if k == 10:
            break


def movie_suggest_caller(input_string):
    movie_suggest()


# * Tell the similar words for given word
def meaning(query):
    reg_ex = re.search(".meaning of (.+)", query)
    print(reg_ex)
    if reg_ex:
        # word_id = reg_ex.group(1)
        ind = query.split().index("of")
        temp = query.split()[ind + 1 :]
        word_id = temp[0]
        print(word_id)
        app_id = "4ea13c64"  # app_id from oxforddictionaries
        app_key = "ee330a18c6d1b84caa707af849421635"  # app_key from oxforddictionaries
        language = "en"
        url = (
            "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
            + language
            + "/"
            + word_id.lower()
        )
        urlFR = (
            "https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/"
            + language
            + "/?corpus=nmc&lemma="
            + word_id.lower()
        )
        r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
        name_json = r.json()
        name_list = []
        for name in name_json["results"]:
            name_list.append(name["word"])
        print("You searched for the word : " + word_id)
        speak("You searched for the word : " + word_id)
        url_mean = (
            "https://od-api.oxforddictionaries.com:443/api/v1/entries/"
            + language
            + "/"
            + word_id.lower()
        )
        mean_json = r.json()
        mean_list = []
        speak("I can Read it out for you")
        for result in mean_json["results"]:
            for lexicalEntry in result["lexicalEntries"]:
                for entry in lexicalEntry["entries"]:
                    for sense in entry["senses"]:
                        mean_list.append(sense["definitions"][0])
                    for i in mean_list:
                        print(word_id + " : " + i)
                        speak(word_id + " : " + i)


def meaning_caller(input_string):
    meaning(input_string)


hash_dict = {
    "open mozila": mozila_caller,
    "open firefox": mozila_caller,
    "open mozila firefox": mozila_caller,
    "start mozila": mozila_caller,
    "start firefox": mozila_caller,
    "start mozila firefox": mozila_caller,
    "tell time": tell_time_caller,
    "what time": tell_time_caller,
    "who is": gk_caller,
    "what is": gk_caller,
    "incremet brightness": brightness_caller,
    "add brightness": brightness_caller,
    "increase brightness": brightness_caller,
    "up brightness": brightness_caller,
    "high brightness": brightness_caller,
    "decrement brightness": brightness_caller,
    "subtract brightness": brightness_caller,
    "decrease brightness": brightness_caller,
    "low brightness": brightness_caller,
    "down brightness": brightness_caller,
    "set brightness": brightness_caller,
    "where": google_map_caller,
    "show in map": google_map_caller,
    "weather": weather_caller,
    "news": news_caller,
    "tell news": news_caller,
    "suggest book": book_suggest_caller,
    "suggest books": book_suggest_caller,
    "suggest top read books": book_suggest_caller,
    "Most read books": book_suggest_caller,
    "suggest top read book": book_suggest_caller,
    "suggest movies": movie_suggest_caller,
    "suggest movies": movie_suggest_caller,
    "suggest top rated movies": movie_suggest_caller,
    "Most imdb star movies": movie_suggest_caller,
    "suggest top rated movie": movie_suggest_caller,
    "corona stats": corona_caller,
    "covid-19 stats": corona_caller,
    "corona virus stats": corona_caller,
    "corona cases' news": corona_caller,
    "number cases corona": corona_caller,
    "tell meaning": meaning_caller,
    "find similar words": meaning_caller,
    "find meaning": meaning_caller,
    "meaning": meaning_caller,
}
