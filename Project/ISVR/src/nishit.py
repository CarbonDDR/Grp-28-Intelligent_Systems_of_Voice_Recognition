"""

Name    -   Nishit Jagetia
ID      -   201801027
Work    -   1) Visual Studio Code app through voice command on different platforms along with the dictionary 
            2) Eclipse app throguh voice command on different platforms along with the dictionary
            Platforms : 
            1 -> MacOS
            2-> Windows
            3-> Linux

"""

import os
from sys import platform
import subprocess


def macvsc():
    #vsc in mac
    os.system('/Applications/Visual Studio Code.app')

def maceclipse():
    #eclipse in mac
    os.system('/Applications/Eclipse.app')

def winvsc():
    #vsc in windows
    subprocess.Popen('user/apps/shortcut/vscode.exe')

def wineclipse():
    #eclipse in windows
    subprocess.Popen('d:/softwares/ecplise/eclipse.exe')

def linvsc():
    #vsc in linux
    subprocess.call('/usr/share/applications/Visual Studio Code.app')

def lineclipse():
    #eclipse in linux
    subprocess.call('/usr/share/applications/Eclipse.app')



# open visual studio code on different platforms
def vscode():
    if platform == "linux" or platform == "linux2":
        # open vscode in linux
        linvsc
    elif platform == "darwin":
        # open vscode in macOS
        macvsc
    elif platform == "win32":
        # opem vscode in windows
        winvsc


# open eclipse on differnet platforms
def eclipse():
    if platform == "linux" or platform == "linux2":
        # open eclipse in linux
        lineclipse
    elif platform == "darwin":
        # open eclipse in macOS
        maceclipse
    elif platform == "win32":
        # open eclipse in windows
        wineclipse



# caller function of vscode
def vsc_caller(query):
    vscode()

# caller function of eclipse
def eclipse_caller(query):
    eclipse()



# dictionary of different words which can be used to call the visual studio code and eclipse app
hash_dict = {

    # dictionary of vscode
    "open vscode" : vsc_caller,
    "open visual studio code" : vsc_caller,
    "open vsc" : vsc_caller,
    "vscode" : vsc_caller,
    "visual studio code" : vsc_caller,
    "vsc" : vsc_caller,
    "start vscode" : vsc_caller,
    "start visual studio code" : vsc_caller,
    "start vsc" : vsc_caller,
    "turn on vscode" : vsc_caller,
    "turn on visual studio code" : vsc_caller,
    "turn on vsc" : vsc_caller,

    # dictionary of eclipse
    "eclipse" : eclipse_caller,
    "open eclipse" : eclipse_caller,
    "start eclipse" : eclipse_caller,
    "turn on eclipse" : eclipse_caller,
    
} 
