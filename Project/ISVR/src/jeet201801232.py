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






def notethat():
    speak("what should i remember sir")
    rememberMessage = ask()
    speak("you said me to remember" + rememberMessage)
    remember = open('data.txt', 'w')
    remember.write(rememberMessage)
    remember.close()

def note_caller(input_string):
    notethat()

def phone_caller(input_string):
    phonelist = []

    def ReadCSVFile():
        global header
        with open('StudentData.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            header = next(csv_reader)
            for row in csv_reader:
                phonelist.append(row)
        set_select()
        print(phonelist)

    def WriteInCSVFile(phonelist):
        with open('StudentData.csv', 'w', newline='') as csv_file:
            writeobj = csv.writer(csv_file, delimiter=',')
            writeobj.writerow(header)
            for row in phonelist:
                writeobj.writerow(row)

    def WhichSelected():
        print("hello", len(select.curselection()))
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name")
        else:
            return int(select.curselection()[0])

    def AddDetail():
        if E_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
            phonelist.append([E_name.get() + ' ' + E_last_name.get(), E_contact.get()])
            print(phonelist)
            WriteInCSVFile(phonelist)
            set_select()
            EntryReset()
            messagebox.showinfo("Confermation", "Succesfully Add New Contact")

        else:
            messagebox.showerror("Error", "Please fill the information")

    def UpdateDetail():
        if E_name.get() and E_last_name.get() and E_contact.get():
            phonelist[WhichSelected()] = [E_name.get() + ' ' + E_last_name.get(), E_contact.get()]
            WriteInCSVFile(phonelist)
            messagebox.showinfo("Confirmation", "Succesfully Update Contact")
            EntryReset()
            set_select()

        elif not (E_name.get()) and not (E_last_name.get()) and not (E_contact.get()) and not (
                len(select.curselection()) == 0):
            messagebox.showerror("Error", "Please fill the information")

        else:
            if len(select.curselection()) == 0:
                messagebox.showerror("Error", "Please Select the Name and \n press Load button")
            else:
                message1 = """To Load the all information of \n 
    						  selected row press Load button\n.
    						  """
                messagebox.showerror("Error", message1)

    def EntryReset():
        E_name_var.set('')
        E_last_name_var.set('')
        E_contact_var.set('')

    def DeleteEntry():
        if len(select.curselection()) != 0:
            result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
            if result == True:
                del phonelist[WhichSelected()]
                WriteInCSVFile(phonelist)
                set_select()
        else:
            messagebox.showerror("Error", 'Please select the Contact')

    def LoadEntry():
        name, phone = phonelist[WhichSelected()]
        print(name.split(' '))
        E_name_var.set(name.split()[0])
        E_last_name_var.set(name.split()[1])
        E_contact_var.set(phone)

    def set_select():
        phonelist.sort(key=lambda record: record[1])
        select.delete(0, END)
        i = 0
        for name, phone in phonelist:
            i += 1
            select.insert(END, f"{i}  |    {name}   |   {phone}")

    window = Tk()

    Frame1 = LabelFrame(window, text="Enter the Contact Detail")
    Frame1.grid(padx=15, pady=15)

    Inside_Frame1 = Frame(Frame1)
    Inside_Frame1.grid(row=0, column=0, padx=15, pady=15)
    # ---------------------------------------------
    l_name = Label(Inside_Frame1, text="Name")
    l_name.grid(row=0, column=0, padx=5, pady=5)
    E_name_var = StringVar()

    E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var)
    E_name.grid(row=0, column=1, padx=5, pady=5)
    # -----------------------------------------------
    l_last_name = Label(Inside_Frame1, text="LastName")
    l_last_name.grid(row=1, column=0, padx=5, pady=5)
    E_last_name_var = StringVar()
    E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var)
    E_last_name.grid(row=1, column=1, padx=5, pady=5)
    # ---------------------------------------------------
    l_contact = Label(Inside_Frame1, text="Contact")
    l_contact.grid(row=2, column=0, padx=5, pady=5)
    E_contact_var = StringVar()
    E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
    E_contact.grid(row=2, column=1, padx=5, pady=5)
    # ---------------------------------------------------
    Frame2 = Frame(window)
    Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)
    # <><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
    Add_button = Button(Frame2, text="Add Detail", width=15, bg="#6B69D6", fg="#FFFFFF", command=AddDetail)
    Add_button.grid(row=0, column=0, padx=8, pady=8)

    Update_button = Button(Frame2, text="Update Detail", width=15, bg="#6B69D6", fg="#FFFFFF", command=UpdateDetail)
    Update_button.grid(row=1, column=0, padx=8, pady=8)

    Reset_button = Button(Frame2, text="Reset", width=15, bg="#6B69D6", fg="#FFFFFF", command=EntryReset)
    Reset_button.grid(row=2, column=0, padx=8, pady=8)
    # ----------------------------------------------------------------------------

    DisplayFrame = Frame(window)
    DisplayFrame.grid(row=1, column=0, padx=15, pady=15)

    scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
    select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 10), bg="#282923", fg="#E7C855",
                     width=40, height=10, borderwidth=3, relief="groove")
    scroll.config(command=select.yview)
    select.grid(row=0, column=0, sticky=W)
    scroll.grid(row=0, column=1, sticky=N + S)

    # -----------------------------------------------------------------------------------
    ActionFrame = Frame(window)
    ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

    Delete_button = Button(ActionFrame, text="Delete", width=15, bg="#D20000", fg="#FFFFFF", command=DeleteEntry)
    Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

    Loadbutton = Button(ActionFrame, text="Load", width=15, bg="#6B69D6", fg="#FFFFFF", command=LoadEntry)
    Loadbutton.grid(row=1, column=0, padx=5, pady=5)
    ReadCSVFile()
    window.mainloop()


hash_dict={
                "show download":show_downloads_caller,"print download": show_downloads_caller,
                "show downloads":show_downloads_caller,"print downloads":show_downloads_caller,
                "display downloads":show_downloads_caller,"display download":show_downloads_caller,
                "take note":note_caller,"note that":note_caller,"remember this":note_caller,
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
                "phone":phone_caller,"contact":phone_caller
               
}
