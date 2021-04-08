import os
from src.va import ask, speak

#createfile function
def deletefile():
    speak("please tell me file name to delete")
    query = ask().lower()
    if os.path.exists(str(query)+".txt"):
        os.remove(str(query)+".txt")
        speak ("file deleted successfully")
        query = query().lower()
    else: 
        speak("file doesnt exist")

            
def delete_caller(query):
    deletefile()
    
hash_dict = {
    "delete file": delete_caller,
    "remove file": delete_caller,
    "file remove": delete_caller,
    "file delete": delete_caller,
    "delete document": delete_caller
    }

#main function

if __name__ == "__main__":
  
  while True:
    query = ask().lower()
    
    if str(query) in query:
      #calling create file function
            speak('deleting file')
            deletefile()






