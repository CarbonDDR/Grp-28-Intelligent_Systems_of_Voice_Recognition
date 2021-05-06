"""
Developer   : Siddharth Moradiya
College ID  : 201801470
About       : This code is useful when user wants to play/open musics or videos or movies.
              This code first ask user to enter what he/she wants to watch (movies,musics or videos).
              Then code helps to find all the available paths in the system.
              User can select perticular folder by entering respective folder number and the code will shows all the available files in that folder.
              Now, user enter the respective file number and system will play that file in default player of the system.
Sources     : Python Documentation
Voice Assistant: https://www.geeksforgeeks.org/voice-assistant-using-python/
"""

import pathlib
import os
import platform
import subprocess
from src.va import ask, speak


## -----------------------Folder finder FOR MOVIES FOLDER------------------------------------------
#This function find the folder from the perticular path
def find_folder(name, path):
    name = name.lower()
    result = []
    for root, dirs, files in os.walk(path,topdown = False):
        dirs = [x.lower() for x in dirs]
        if name in dirs:
            result.append(os.path.join(root, name))
    return result


#This function collects all the paths of the folder with  "perticular name"
def folder_finder():
    speak("please specify the folder name which contains Movies Videos or Musics")
    file_k = ask()
    file_names = [file_k.lower()]
    if(file_k[-1]!='s'): 
        file_names.append(file_k.lower()+'s')
    
    sysos = platform.system()
    found_paths = []
    if sysos == "Windows":
        drive_latter = os.popen("fsutil fsinfo drives").readlines()
        drive_latter = drive_latter[1].split(' ')
        drive_latter.pop(0)
        drive_latter.pop(-1)

        for file_name in file_names:  
            for drive_path in drive_latter:  
                found_paths.extend(find_folder(file_name,drive_path))
    elif sysos == "Linux":
        found_paths = find_folder(file_name,"//")
    elif sysos == "Darwin":
        found_paths =  find_folder(file_name,"//")
    
    if len(found_paths)==0:
        speak('Sorry, system cannot find your folder. Please try again.')
    elif len(found_paths) == 1:
        speak('Here System found only one folder with given file name')
        print('Here System found only one folder with given file name : ',file_k)
        ff=found_paths[0]
    else:
        speak('System found This many path, from which path you want to play')
        print('System found This many path from which you want to play', file_k.capitalize())
        print('\n***************************')
        for i in range(0,len(found_paths)):
            print(i+11,' : ',found_paths[i])
        print('***************************')
        speak('Please provide the Number of the file')
        
        ff = found_paths[int(ask())-11]
        print("\033[1m", '\nPlease provide the Number of the file :',"\033[0m")
    return ff
## -----------------------Folder finder FOR MOVIES FOLDER------------------------------------------



# This function is used to see the list of the available files in perticular path.
def print_dict(t): 
    c = 0
    print('\n***************************')
    for i in range(len(t)):
        print(c+11,':',t[c])
        c+=1
    print('***************************\n')

#All the process is done by the below function
def player():
    file_path_video = folder_finder()

    flist_video = [p for p in pathlib.Path(file_path_video).iterdir() if p.is_file()]
    f_video = []
    filename = {}

    c = 0 
    for f in flist_video:
        f_video.append('"'+ str(f) +'"')
        stemp, ftemp = os.path.split(str(f))
        filename[c] = str(ftemp)
        c+=1

    print_dict(filename)
    t = int(ask())-11
    os.system(f_video[t])


def player_caller():
    player()


hash_dict = {
    "play musics": player_caller,
    "play movies": player_caller,
    "play videos": player_caller,
    "open musics": player_caller,
    "open movies": player_caller,
    "open videos": player_caller,
    "start musics": player_caller,
    "start movies": player_caller,
    "start videos": player_caller,
    }



# if __name__ == "__main__":
#     player_caller()

