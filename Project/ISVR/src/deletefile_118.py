import os
from src.va import ask, speak


def identify_extension(query):
  if query == 'text':
    return ".txt"
  if query == 'document':
    return ".doc"
  if query == 'python':
    return '.py'
  if query == 'javascript':
    return '.js'
  if query == 'ppt':
    return '.pptx'
  if query =='c plus plus':
    return '.cpp'
  if query == 'none':
    return ''
  else:
    return ("." + query)


#delete file function
def deletefile():
    speak("please tell me file name to delete")
    query = ask().lower()
    speak("please tell the file extension")
    ext = ask().lower()
    ext = identify_extension(ext)
    query = query+ext
    if os.path.exists(str(query)):
        os.remove(str(query))
        speak ("file deleted successfully")
        query = query.lower()
    else: 
        speak("file doesnt exist")


def delete_caller(query):
    deletefile()
    
hash_dict = {
    "delete file": delete_caller,
    "remove file": delete_caller,
    "delete doc": delete_caller,
    "remove doc": delete_caller,
    "delete text": delete_caller,
    "remove text": delete_caller,
    "delete document": delete_caller,
    "remove document": delete_caller,
    "delete ppt": delete_caller,
    "remove ppt": delete_caller,
    "delete powerpoint": delete_caller,
    "remove powerpoint": delete_caller,
    "delete css": delete_caller,
    "remove css": delete_caller,
    "delete javascript": delete_caller,
    "remove javascript": delete_caller,
    "delete python": delete_caller,
    "remove python": delete_caller,
    "delete java": delete_caller,
    "remove java": delete_caller,
    "delete cpp": delete_caller,
    "remove cpp": delete_caller,
    "delete html": delete_caller,
    "remove html": delete_caller,
    "delete pdf": delete_caller,
    "remove pdf": delete_caller
    }

#main function
if __name__ == "__main__":
  
  while True:
    query = ask().lower()
    
    if str(query) in query:
      #calling create file function
            speak('deleting file')
            deletefile()



