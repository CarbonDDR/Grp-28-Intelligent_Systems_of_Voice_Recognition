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


 #createfile function
def createfile():
  speak("please tell me file name")
  query = ask().lower()
  speak("Tell the file type that you want to create")
  ext = ask().lower()
  ext = identify_extension(ext)
  query = query+ext
  f=open(query,"w")
  speak ("file created successfully. please tell me what do you want to write ")
  query = ask().lower()
  f.write(str(query))
  speak("file created")  
      

def create_caller(query):
    createfile()

hash_dict = {
    "create file": create_caller,
    "make file": create_caller,
    "create doc": create_caller,
    "make doc": create_caller,
    "create text": create_caller,
    "make text": create_caller,
    "create document": create_caller,
    "make document": create_caller,
    "create ppt": create_caller,
    "make ppt": create_caller,
    "create powerpoint": create_caller,
    "make powerpoint": create_caller,
    "create css": create_caller,
    "make css": create_caller,
    "create javascript": create_caller,
    "make javascript": create_caller,
    "create python": create_caller,
    "make python": create_caller,
    "create java": create_caller,
    "make java": create_caller,
    "create cpp": create_caller,
    "make cpp": create_caller,
    "create html": create_caller,
    "make html": create_caller,
    "create pdf": create_caller,
    "make pdf": create_caller
    }
#main function
if __name__ == "__main__":
  
  while True:
    query = ask().lower()
    
    if str(query) in query:
      #calling create file function
            speak('creating file')
            createfile()
            






