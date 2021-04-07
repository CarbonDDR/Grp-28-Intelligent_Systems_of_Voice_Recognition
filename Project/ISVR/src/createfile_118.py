# import important models
import speech_recognition as sr 
import pyttsx3  

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
def createfile():
  speak("please tell me file name")
  query = takeCommand().lower()
  f=open(str(query)+".txt","w")
  speak ("file created successfully. please tell me what do you want to write ")
  query = takeCommand().lower()
  f.write(str(query))
  speak("file created")
    #main function
if __name__ == "__main__":
  
  while True:
    query = takeCommand().lower()
    
    if str(query) in query:
      #calling create file function
            speak('creating file')
            createfile()
            
def create_caller():
    createfile()
    
hash_dict = {
    "create file": create_caller,
    "make file": create_caller,
    "file create": create_caller,
    "file make": create_caller,
    "create document": create_caller
    }





