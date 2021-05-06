"""
Developer   : Aakash Panchal
College ID  : 201801459
About       : Added file and folder finder, which searches for a given file(or folder) among all the files or 
              folders on the pc. In case there are multiple files or folders with
              the same name, then it will print all the paths of found files or folders.
Update      : If there are multiple files with the same name, then you can specify the file you want to open.
Sources     : Python Documentation
"""

import os
import platform
import subprocess
from src.va import ask, speak


## -----------------------Folder finder START------------------------------------------
def find_folder(name, path):
    name = name.lower()
    result = []
    for root, dirs, files in os.walk(path,topdown = False):
        dirs = [x.lower() for x in dirs]
        if name in dirs:
            result.append(os.path.join(root, name))
    return result

def folder_finder(speak):
    print("please specify the folder name")
    file_name = None
    while True:
      file_name = ask()
      if file_name == "":
        continue
      else:
        break
    #file_name = ask()
    sysos = platform.system()

    if sysos == "Windows":
        found_paths = find_folder(file_name,"\\")
    elif sysos == "Linux":
        found_paths = find_folder(file_name,"//")
    elif sysos == "Darwin":
        found_paths =  find_folder(file_name,"//")
        
    if len(found_paths) == 0:
        speak("No such folder found")
    elif len(found_paths) == 1:
        os.startfile(found_paths[0])
    else:
        j = 1
        for line in found_paths:
            print(str(j) + '.', line)
            j += 1
        print("There are multiple folders with this name. Please specify the id of the path you want to open.")
        number = int(ask())
        os.startfile(found_paths[number - 1])
## -----------------------Folder finder END------------------------------------------


## -----------------------File finder START------------------------------------------
        
def Linux(file_name):
    cmd = subprocess.Popen(f"find . -name {file_name}", shell=True, stdout=subprocess.PIPE)
    subprocess_return = cmd.communicate()
    ans = subprocess_return[0].decode("utf-8")
    paths = []
    for line in ans.split('\n'):
        paths.append(line)
    paths.pop()
    
    if len(paths) == 0:
        speak("No such file found")
    elif len(paths) == 1:
        subprocess.Popen(f"xdg-open {paths[0]}", shell=True, stdout=subprocess.PIPE)
    else:
        j = 1
        for line in paths:
            print(str(j) + '.', line)
            j += 1
        print("There are multiple files with this name. Please specify the id of the path you want to open.")
        number = int(ask())
        os.startfile(paths[number - 1])

def Windows(file_name):
    cmd = subprocess.Popen(f"where /r \ {file_name}", shell=True, stdout=subprocess.PIPE)
    subprocess_return = cmd.communicate()
    ans = subprocess_return[0].decode("utf-8")
    paths = []
    for line in ans.split('\n'):
        paths.append(line)
    paths.pop()
    for line in paths:
        line = line[:-1]
    
    if len(paths) == 0:
        speak("No such file found")
    elif len(paths) == 1:
        subprocess.Popen(paths[0], shell=True, stdout=subprocess.PIPE)
    else:
        j = 1
        for line in paths:
            print(str(j) + '.', line)
            j += 1
        print("There are multiple files with this name. Please specify the id of the path you want to open.")
        number = int(ask())
        os.startfile(paths[number - 1])

def Macos(file_name):
    cmd = subprocess.Popen(f"find / -name {file_name}", shell=True, stdout=subprocess.PIPE)
    subprocess_return = cmd.communicate()
    ans = subprocess_return[0].decode("utf-8")
    paths = []
    for line in ans.split('\r'):
        paths.append(line)
    paths.pop()
    
    if len(paths) == 0:
        print("No such file found")
    elif len(paths) == 1:
        subprocess.Popen(f"open {paths[0]}", shell=True, stdout=subprocess.PIPE)
    else:
        j = 1
        for line in paths:
            print(str(j) + '.', line)
            j += 1
        print("There are multiple files with this name. Please specify the id of the path you want to open.")
        number = int(ask())
        os.startfile(paths[number - 1])
        
def file_finder(speak):
    print("please specify the file name without extension")
    file_name = None
    while True:
      file_name = ask()
      if file_name == "":
        continue
      else:
        break
    
    print("please specify the extension")
    extension = None
    while True:
      extension = ask()
      if extension == "":
        continue
      else:
        break
    file_name = file_name + "." + extension
    
    sysos = platform.system()
    if sysos == "Windows":
        Windows(file_name)
    elif sysos == "Linux":
        Linux(file_name)
    elif sysos == "Darwin":
        Macos(file_name)

## -----------------------File finder END------------------------------------------

hash_dict = {
    "find folder" : folder_finder,
    "search folder" : folder_finder,
    "find file" : file_finder,
    "search file" : file_finder,
    "open folder" : folder_finder,
    "open file" : file_finder
}
