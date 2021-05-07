"""
Name: Parthav Kansagra
  ID: 201801145
"""
import webbrowser
import os
from tkinter import *
import time


def webex():
    webbrowser.open("https://www.webex.com")


def webex_caller(query):
    webex()


def timer_submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:

            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up ")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


def timer():
    root = Tk()

    # setting geometry of tk window
    root.geometry("300x250")

    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    root.title("Time Counter")

    # Declaration of variables
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
    hourEntry.place(x=80, y=20)

    minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=130, y=20)

    secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
    secondEntry.place(x=180, y=20)

    # button widget
    btn = Button(root, text="Set Time Countdown", bd="5", command=timer_submit)
    btn.place(x=70, y=120)

    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()


def timer_caller(input_string):
    timer()


def Rock_Paper_Scissors():
    import sys
    import tkinter.messagebox

    from random import randrange

    root = Tk()
    root.geometry("300x150+0+0")
    playerChoice = StringVar(None)
    result = StringVar(None)
    win = "You win"
    tie = "Its a tie!"
    lose = "You lose"

    scissorsgif = PhotoImage(file="scissors.gif")
    papergif = PhotoImage(file="paper.gif")
    stonegif = PhotoImage(file="stone.gif")

    def Rock():
        CPUChoice = randrange(3)
        playerChoice = "1"
        if playerChoice == "1" and CPUChoice == 0:
            result = tie
            resultText.set("You and the CPU both picked rock. " + result)

        if playerChoice == "1" and CPUChoice == 1:
            result = lose
            resultText.set("Paper beats rock. " + result)

        if playerChoice == "1" and CPUChoice == 2:
            result = win
            resultText.set("Rock smashes scissors. " + result)

    def Paper():
        CPUChoice = randrange(3)
        playerChoice = "2"
        if playerChoice == "2" and CPUChoice == 0:
            result = win
            resultText.set("Paper beats rock. " + result)

        if playerChoice == "2" and CPUChoice == 1:
            result = tie
            resultText.set("You and the CPU both picked paper " + result)

        if playerChoice == "2" and CPUChoice == 2:
            result = lose
            resultText.set("Scissors cuts up paper. " + result)

    def Scissors():
        CPUChoice = randrange(3)
        playerChoice = "3"
        if playerChoice == "3" and CPUChoice == 0:
            result = lose
            resultText.set("Rock smashes scissors. " + result)

        if playerChoice == "3" and CPUChoice == 1:
            result = win
            resultText.set("Scissors cuts up paper. " + result)

        if playerChoice == "3" and CPUChoice == 2:
            result = tie
            resultText.set("You and the CPU both picked scissors. " + result)

    widgetRock = Button(root, command=Rock, width=40, height=35, image=stonegif)
    widgetRock.place(x=25, y=10)

    widgetPaper = Button(root, command=Paper, width=40, height=35, image=papergif)
    widgetPaper.place(x=125, y=10)

    widgetS = Button(root, command=Scissors, width=40, height=35, image=scissorsgif)
    widgetS.place(x=225, y=10)

    resultText = StringVar()
    resultText.set("Go!")
    widgetResult = Label(root, textvariable=resultText, width=42)
    widgetResult.place(x=0, y=70)

    widgetE = Button(root, text="End Game", command=quit, width=20)
    widgetE.place(x=75, y=110)

    root.title("Rock, Paper, Scissors!")
    root.mainloop()


def Rock_Paper_Scissors_Caller(input_string):
    Rock_Paper_Scissors()


hash_dict = {
    "open webex": webex_caller,
    "webex": webex_caller,
    "open webex meeting": webex_caller,
    "open timer": timer_caller,
    "set timer": timer_caller,
    "open game rock paper scissors": Rock_Paper_Scissors_Caller,
    "open rock paper scissors": Rock_Paper_Scissors_Caller,
    "start game rock paper scissors": Rock_Paper_Scissors_Caller,
    "start rock paper scissors": Rock_Paper_Scissors_Caller,
}
