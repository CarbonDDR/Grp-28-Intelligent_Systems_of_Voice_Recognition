import psutil
import os
import webbrowser
import random
import string
from sys import platform
import psutil as p
from src.va import speak,ask

def downloads_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def show_downloads():
    path_of_download=downloads_path()
    total_list=os.listdir(path_of_download)
    print(total_list)

def  show_downloads_caller(input_string):
    show_downloads()


def size(byte):
  #this the function to convert bytes into more suitable reading format.

  #Suffixes for the size
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

def disk():
    print("-" * 50, "Disk Information", "-" * 50)
    print("Partitions on Drive:")

    par = p.disk_partitions()
    for x in par:
        print("Drive: ", x.device)
        print("  File system type: ", x.fstype)

        dsk = p.disk_usage(x.mountpoint)
        print("  Total Size: ", size(dsk.total))
        print("  Used:       ", size(dsk.used))
        print("  Free:       ", size(dsk.free))
        print("  Percentage: ", dsk.percent, "%\n")

def disk_caller(input_string):
     disk()



def memory():
  print("-"*50, "Memory Information", "-"*50)

  #Getting the Memory/Ram Data.
  mem = p.virtual_memory()
  print("Total Memory:    ",size(mem.total))
  print("Available Memory:", size(mem.available))
  print("Used Memory:     ", size(mem.used))
  print("Percentage:      ",mem.percent,"% \n")

  #It is the Hard disk/ SSD space Which is used up as main memory when the main memory is not sufficient.
  print("-"*48, "Swap Memory Information", "-"*47)
  swmem = p.swap_memory()
  print("Total Memory:    ", size(swmem.total))
  print("Available Memory:", size(swmem.free))
  print("Used Memory:     ", size(swmem.used))
  print("Percentage:      ", swmem.percent, "%\n")

def memory_caller(input_string):
    memory()

def cpu():
  print("-"*50, "CPU Information", "-"*50)


  print("Logical/Total Core Count: ", p.cpu_count(logical=True) )
  print("Physical Core Count: ", p.cpu_count(logical=False))
  fre=p.cpu_freq()
  print("Maximum Frequency:" ,fre.max, "Mhz")
  print("Minimum Frequency:", fre.min,"Mhz")
  print("Current Frequency: ",fre.current ,"Mhz")

  for x, percentage_usage in enumerate(p.cpu_percent(percpu=True)):
      print("Core ",x, ":",percentage_usage,"%")
  print("Total CPU Usage:", p.cpu_percent(),"%\n")

def cpu_caller(input_string):
    cpu()


def pasword():

        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        speak("please enter password length")
        plen = int(input("Enter password length\n"))

        s=[]
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
        p=("".join(random.sample(s, plen)))
        print(p)


def password_caller(input_string):
    pasword()



def show_battery():

    speak("Showing remaining battery")
    battery = psutil.sensors_battery()
    percent = battery.percent
    percentinletters = str(percent)
    speak(
        "Sir, there is " + percentinletters + " percent remaining. Battery remaining is printed in the main screen.")
    print("There is " + percentinletters + " % remaining.")
    print("")


def battery_caller(input_string):
    show_battery()



def open_location():
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab('https://google.nl/maps/place')
    speak('Here is the location ')


def location_caller(input_string):
    open_location()


def notethat():
    speak("what should i remember sir")
    rememberMessage = ask()
    speak("you said me to remember" + rememberMessage)
    remember = open('data.txt', 'w')
    remember.write(rememberMessage)
    remember.close()

def note_caller(input_string):
    notethat()


def mozela():
    if platform == "linux" or platform == "linux2":
        subprocess.run('firefox',shell=True)
    elif platform == "darwin":
        subprocess.run('open -a Firefox --args -private-window',shell=True)
    elif platform == "win32":
        subprocess.run('start firefox',shell=True)
    else:
        speak("Unsupported OS")

def mozela_caller(input_string):
    mozela()


hash_dict={
                "open mozela":mozela_caller,"open firefox":mozela_caller,"open mozela firefox":mozela_caller,
                "start mozela":mozela_caller,"start firefox":mozela_caller,"start mozela firefox":mozela_caller,
                "show download":show_downloads_caller,"print download": show_downloads_caller,
                "show downloads":show_downloads_caller,"print downloads":show_downloads_caller,
                "display downloads":show_downloads_caller,"display download":show_downloads_caller,
                "take note":note_caller,"note that":note_caller,"remember this":note_caller,
                 "my location":location_caller,"open location":location_caller, 
                "display location":location_caller,"fetch location":location_caller,"show location":location_caller,
                 "remaining battery":battery_caller,  "display  cpu":cpu_caller,"information cpu":cpu_caller,"show cpu":cpu_caller,
                 "cpu usage":cpu_caller,"data  cpu":cpu_caller,"information cpu":cpu_caller,"display cpu":cpu_caller,
                 "details cpu":cpu_caller,"statistics cpu":cpu_caller,
                 "frequency  cpu":cpu_caller," cores cpu":cpu_caller,
                 "display  drive": disk_caller, "information  drive": disk_caller, "show  drive": disk_caller,
                "drive usage": disk_caller,  "data  drives": disk_caller,
                "details  drive": disk_caller, "statistics  drive": disk_caller,
                "display  disk": disk_caller, "information disk": disk_caller, 
                "disk usage": disk_caller, "data  disk": disk_caller,
                "details  disk": disk_caller, "statistics  disk": disk_caller, 
               "display  memory": memory_caller, "information memory": memory_caller, "show  memory": memory_caller,
              "memory usage": memory_caller,"data  memory": memory_caller,
               "details  memory": memory_caller, "statistics  memory": memory_caller, "memory details": memory_caller,
               "generate password":password_caller,"create password":password_caller,
                "produce password":password_caller, "make password":password_caller,"form password":password_caller,
               
}
