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
from tkinter import *
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
        print("Do you want to speak again? Yes/No:")
        if ask().lower() == "no":
            break
        else:
            continue
    #file_name = ask()
    sysos = platform.system()

    if sysos == "Windows":
        found_paths = find_folder(file_name,"\\")
    elif sysos == "Linux":
        found_paths = find_folder(file_name,"//")
    elif sysos == "Darwin":
        found_paths =  find_folder(file_name,"//")
        
    if len(found_paths) == 0:
        print("No such folder found")
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
        print("No such file found")
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
        print("No such file found")
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
        print("Do you want to speak again? Yes/No:")
        if ask().lower() == "no":
            break
        else:
            continue
    
    print("please specify the extension")
    extension = None
    while True:
      extension = ask()
      if extension == "":
        continue
      else:
        print("Do you want to speak again? Yes/No:")
        if ask().lower() == "no":
            break
        else:
            continue
    file_name = file_name + "." + extension
    
    sysos = platform.system()
    if sysos == "Windows":
        Windows(file_name)
    elif sysos == "Linux":
        Linux(file_name)
    elif sysos == "Darwin":
        Macos(file_name)

## -----------------------File finder END------------------------------------------

## ----------------------- Unit converter START-------------------------------------------

# Conversion factors
unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592,
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "are" : 100.0,
    "hectare" : 10000.0,
    "acre": 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "km", "feet", "miles", "inches",]
weights = ["kg", "grams", "quintals", "tonnes", "pounds",]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]

# Options for drop-down menu
OPTIONS = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit",
            "sq. m",
            "sq. km",
            "are",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]
    
    
def ok():
    inp = float(inputentry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights,
    inp_unit in temps and out_unit in temps,
    inp_unit in areas and out_unit in areas,
    inp_unit in volumes and out_unit in volumes]

    if any(cons): # If both the units are of same type, do the conversion
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp - 32) * (5/9))
        else:
            outputentry.delete(0, END)
            outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

    else: # Display error if units are of different types
        outputentry.delete(0, END)
        outputentry.insert(0, "ERROR")
        
        
        
def unit_converter():
    root = Tk()
    root.geometry("400x300")
    root.title("Unit Converter")
    root['bg'] = 'black'
    
    inputopt = StringVar()
    inputopt.set(OPTIONS[0])

    outputopt = StringVar()
    outputopt.set(OPTIONS[0])

    # Widgets
    inputlabel = Label(root, text = "Input")
    inputlabel.grid(row = 0, column = 0, pady = 20)

    inputentry = Entry(root, justify = "center", font = "bold")
    inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

    inputmenu = OptionMenu(root, inputopt, *OPTIONS)
    inputmenu.grid(row = 1, column = 1)
    inputmenu.config(font = "Arial 12")

    outputlabel = Label(root, text = "Output")
    outputlabel.grid(row = 2, column = 0, pady = 20)

    outputentry = Entry(root, justify = "center", font = "bold")
    outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

    outputmenu = OptionMenu(root, outputopt, *OPTIONS)
    outputmenu.grid(row = 3, column = 1)
    outputmenu.config(font = "Arial 12")

    okbtn = Button(root, text = "OK", command = ok, padx = 80, pady = 2)
    okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

    root.mainloop()
## ----------------------- Unit converter END-------------------------------------------

hash_dict = {
    "find folder" : folder_finder,
    "search folder" : folder_finder,
    "find file" : file_finder,
    "search file" : file_finder,
    "open folder" : folder_finder,
    "open file" : file_finder,
    "unit convert" : unit_converter,
    "unit converter" : unit_converter,
    "convert unit" : unit_converter
}
