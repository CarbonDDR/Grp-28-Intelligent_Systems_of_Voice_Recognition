# import important models
import speech_recognition as sr 
import pyttsx3  
import os

#important properties
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()  

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#hear function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
    return query


   #createfile function
def deletefile():
    speak("please tell me file name to delete")
    query = takeCommand().lower()
    if os.path.exists(str(query)+".txt"):
        os.remove(str(query)+".txt")
        speak ("file deleted successfully")
        query = takeCommand().lower()
    else: 
        speak("file doesnt exist")


    #main function
if __name__ == "__main__":
  
  while True:
    query = takeCommand().lower()
    
    if str(query) in query:
      #calling create file function
            speak('deleting file')
            deletefile()
            
def delete_caller():
    deletefile()
    
hash_dict = {
    "delete file": delete_caller,
    "remove file": delete_caller,
    "file remove": delete_caller,
    "file delete": delete_caller,
    "delete document": delete_caller
    }









