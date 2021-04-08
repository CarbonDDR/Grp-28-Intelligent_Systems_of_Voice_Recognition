import os
from src.va import ask, speak


#createfile function
def createfile():
  speak("please tell me file name")
  query = ask().lower()
  f=open(str(query)+".txt","w")
  speak ("file created successfully. please tell me what do you want to write ")
  query = ask().lower()
  f.write(str(query))
  speak("file created")

            
def create_caller(query):
    createfile()
    
hash_dict = {
    "create file": create_caller,
    "make file": create_caller,
    "file create": create_caller,
    "file make": create_caller,
    "create document": create_caller
    }

#main function
if __name__ == "__main__":
  
  while True:
    query = ask().lower()
    
    if str(query) in query:
      #calling create file function
            speak('creating file')
            createfile()




