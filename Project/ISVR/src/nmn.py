import pyjokes
import json
import wolframalpha
from src.va import speak, ask

WFA_KEY_JSON = 'src/wolf_key.json'


def tell_joke():
    speak(pyjokes.get_joke())

def eval_s_caller(query):
    
    app_id = json.load(open(WFA_KEY_JSON, 'r'))['APPID']
    client = wolframalpha.Client(app_id)
    if 'calculate' in query.lower():
        indx = query.lower().split().index('calculate')
    elif 'evaluate' in query.lower():
        indx = query.lower().split().index('evaluate')

    try:
        query = query.split()[indx + 1:]
    except:
        speak("Could you please specify what to calculate?")
        query = ask()
    res = client.query(' '.join(query))
    try:
        answer = next(res.results).text
    except:
        speak("No responce from the API")
        return
    print("The answer is " + answer)
    speak("The answer is " + answer)

def tell_joke_caller(query):
    tell_joke()

dict1 = {
    "evaluate": eval_s_caller,
    "calculate": eval_s_caller,
    "tell joke": tell_joke_caller
}
