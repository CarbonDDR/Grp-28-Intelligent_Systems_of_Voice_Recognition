"""

Name    -   Nishit Jagetia
ID      -   201801027
Work    -   1) Visual Studio Code app through voice command on all platforms along with the dictionary 
            2) Eclipse app throguh voice command on mac and linux along with the dictionary
            3) Xcode app through voice command in mac along with the dictionary
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
    os.system('open /Applications/Visual\ Studio\ Code.app')

def maceclipse():
    #eclipse in mac
    os.system('open /Applications/Eclipse.app')

def winvsc():
    #vsc in windows
    os.system('code')

def wineclipse():
    #eclipse in windows
    #enter path
    subprocess.Popen('path')

def linvsc():
    #vsc in linux
    subprocess.call('code')

def lineclipse():
    #eclipse in linux
    #enter path
    subprocess.call('path')

def macxcode():
    #xcode in mac
    os.system('open /Applications/Xcode.app')


# open visual studio code on different platforms
def vscode():
    if platform == "linux" or platform == "linux2":
        linvsc()
    elif platform == "darwin":
        macvsc()
    elif platform == "win32":
        winvsc()


# open eclipse on differnet platforms
def eclipse():
    if platform == "linux" or platform == "linux2":
        lineclipse()
    elif platform == "darwin":
        maceclipse()

def xcode():
    if platform == "darwin":
        macxcode()


# caller function of vscode
def vsc_caller(query):
    vscode()

# caller function of eclipse
def eclipse_caller(query):
    eclipse()

def xcode_caller(query):
    xcode()



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
    
    #dictionary of xcode
    "xcode" : xcode_caller,
    "start xcode" : xcode_caller,
    "turn on xcode" : xcode_caller,
    "open xcode" : xcode_caller
} 

#xcode_caller("open")
#vsc_caller("open")
#eclipse_caller("open")
