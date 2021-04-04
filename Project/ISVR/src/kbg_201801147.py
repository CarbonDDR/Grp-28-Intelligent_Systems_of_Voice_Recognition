import os
import platform


def openTextEditor():
    pt = platform.system()
    if pt == 'win32' or pt == 'Windows':
        os.system('notepad')
    elif pt == 'linux' or pt == 'linux2' or pt == 'Linux':
        os.system('gedit')


def open_caller(line):
    openTextEditor()


hash_dict = {
    "open notepad": open_caller,
    "start notepad": open_caller,
    "open text editor": open_caller,
    "start text editor": open_caller,
    "open gedit": open_caller,
    "start gedit": open_caller,
    "notepad": open_caller,
    "notepad start": open_caller,
    "notepad open": open_caller,
    "text editor": open_caller,
    "gedit open": open_caller,
    "gedit start": open_caller,
    "gedit": open_caller,
    "text editor start": open_caller,
    "text editor open": open_caller
}

# open_caller("open")
