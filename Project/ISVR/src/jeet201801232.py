import psutil
import os
import webbrowser
import random
import string
from sys import platform
import psutil as p
from va import speak,ask

def show_downloads():
    if platform == "linux" or platform == "linux2":
        download_dir = "home\\jeetumat\\Downloads"
        total_list = os.listdir(download_dir)
        print(total_list)
    elif platform == "win32":
        download_dir = "C:\\Users\\Jeet\\Downloads"
        total_list = os.listdir(download_dir)
        print(total_list)
    elif platform == "darwin":
        download_dir = "Users/Jeet/Downloads"
        total_list = os.listdir(download_dir)
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
        # print(s,"\n")
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


hash_dict={
                "show download":show_downloads_caller,"print download": show_downloads_caller,
                "show downloads":show_downloads_caller,"print downloads":show_downloads_caller,
                "fetch downloads":show_downloads_caller,"fetch download":show_downloads_caller,
                "display downloads":show_downloads_caller,"display download":show_downloads_caller,
                "take note":note_caller,"note that":note_caller,"remember this":note_caller,
                 "my location":location_caller,"open location":location_caller, "display my location":location_caller,
                "display location":location_caller,"fetch location":location_caller,
                 "remaining battery":battery_caller,  "display  cpu":cpu_caller,"information  cpu":cpu_caller,"show  cpu":cpu_caller,
                 "cpu usage":cpu_caller,"data  cpu":cpu_caller,
                 "details  cpu":cpu_caller,"statistics cpu":cpu_caller,"fetch cpu details":cpu_caller,
                 "frequency  cpu":cpu_caller," cores in cpu":cpu_caller,"details of cores":cpu_caller,
                 "display about drive": disk_caller, "information  drive": disk_caller, "show about drive": disk_caller,
                "drive usage": disk_caller,  "data of drives": disk_caller,
                "details of drive": disk_caller, "statistics of drive": disk_caller, "fetch drive details": disk_caller,
                "display about disk": disk_caller, "information of disk": disk_caller, "show about disk": disk_caller,
                "disk usage": disk_caller, "fetch disk usage": disk_caller, "data of disk": disk_caller,
                "details of disk": disk_caller, "statistics of disk": disk_caller, "fetch disk details": disk_caller,
               "display about memory": memory_caller, "information of memory": memory_caller, "show about memory": memory_caller,
              "memory usage": memory_caller,"data about memory": memory_caller,
               "details of memory": memory_caller, "statistics of memory": memory_caller, "fetch memory details": memory_caller,
               "generate password":password_caller,"initiate password":password_caller,"create password":password_caller,
                "produce password":password_caller, "make password":password_caller,"form password":password_caller,
                "construct password":password_caller,"build password":password_caller,
}
