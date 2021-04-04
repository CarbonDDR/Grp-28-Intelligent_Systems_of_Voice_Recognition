"""
Developer   : Aakash Panchal
College ID  : 201801459
About       : Added file and folder finder, which searches for a given file(or folder) among all the files or 
              folders on the pc. In case there are multiple files or folders with
              the same name, then it will print all the paths of found files or folders.
Sources     : Python Documentation
"""

import os
import platform
import subprocess


## -----------------------Folder finder START------------------------------------------
def find_folder(name, path):
    name = name.lower()
    result = []
    for root, dirs, files in os.walk(path,topdown = False):
        dirs = [x.lower() for x in dirs]
        if name in dirs:
            result.append(os.path.join(root, name))
    return result
    
# Protocol: "Open {folder_name} folder"
def process_for_folder(string):
    parts = string.split(" ")
    return parts[1]
    
def folder_finder(speak):
    file_name = process_for_folder(speak)
    sysos = platform.system()

    if sysos == "Windows":
        found_paths = find_folder(file_name,"\\")
    elif sysos == "Linux":
        found_paths = find_folder(file_name,"//")
    elif sysos == "Darwin":
        found_paths =  find_folder(file_name,"//")

    if len(found_paths) == 1:
        os.startfile(found_paths[0])
    else:
        for line in found_paths:
            print(line)
        input("")
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
    if len(paths) == 1:
        subprocess.Popen(f"xdg-open {paths[0]}", shell=True, stdout=subprocess.PIPE)
    else:
        for line in paths:
            print(line)
        input("")

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
    if len(paths) == 1:
        subprocess.Popen(paths[0], shell=True, stdout=subprocess.PIPE)
    else:
        for line in paths:
            print(line)
        input("")

def Macos(file_name):
    cmd = subprocess.Popen(f"find / -name {file_name}", shell=True, stdout=subprocess.PIPE)
    subprocess_return = cmd.communicate()
    ans = subprocess_return[0].decode("utf-8")
    paths = []
    for line in ans.split('\r'):
        paths.append(line)
    paths.pop()
    if len(paths) == 1:
        subprocess.Popen(f"open {paths[0]}", shell=True, stdout=subprocess.PIPE)
    else:
        for line in paths:
            print(line)
        input("")

# Extension must be spelled with the file name
# Find a word with having '.' as a character.
def process_for_file(string):
    parts = string.split(" ")
    for word in parts:
        if word.find(".") != -1:
            return word

def file_finder(speak):
    file_name = process_for_file(speak)
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
    "open folder" : folder_finder,
    "find file" : file_finder,
    "open file" : file_finder
}