"""

Name    -   Nishit Jagetia
ID      -   201801027
Work    -   1) Visual Studio Code app through voice command on all platforms along with the dictionary 
            2) Eclipse app throguh voice command on mac and linux along with the dictionary
            3) Xcode app through voice command in mac along with the dictionary
            4) Made loan calculator app, works on all platform
            Platforms : 
            1 -> MacOS
            2-> Windows
            3-> Linux


"""
# importing required libraries
# run pip3 install pyqt5 before this
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
from sys import platform
import subprocess
import sys


class Window(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # width of window
        self.w_width = 400

        # height of window
        self.w_height = 500

        # setting geometry
        self.setGeometry(100, 100, self.w_width, self.w_height)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for adding components
    def UiComponents(self):
        # creating head label
        head = QLabel("Loan Calculator", self)

        # setting geometry to the head
        head.setGeometry(0, 10, 400, 60)

        # font
        font = QFont("Times", 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # setting font to the head
        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)

        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)

        # creating a interest label
        i_label = QLabel("Annual Interest", self)

        # setting properties to the interest label
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20, 100, 170, 40)
        i_label.setStyleSheet(
            "QLabel"
            "{"
            "border : 2px solid black;"
            "background : rgba(70, 70, 70, 35);"
            "}"
        )
        i_label.setFont(QFont("Times", 9))

        # creating a QLineEdit object to get the interest
        self.rate = QLineEdit(self)

        # accepting only number as input
        onlyInt = QIntValidator()
        self.rate.setValidator(onlyInt)

        # setting properties to the rate line edit
        self.rate.setGeometry(200, 100, 180, 40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont("Times", 9))

        # creating a number of years label
        n_label = QLabel("Years ", self)

        # setting properties to the years label
        n_label.setAlignment(Qt.AlignCenter)
        n_label.setGeometry(20, 150, 170, 40)
        n_label.setStyleSheet(
            "QLabel"
            "{"
            "border : 2px solid black;"
            "background : rgba(70, 70, 70, 35);"
            "}"
        )
        n_label.setFont(QFont("Times", 9))

        # creating a QLineEdit object to get the years
        self.years = QLineEdit(self)

        # accepting only number as input
        onlyInt = QIntValidator()
        self.years.setValidator(onlyInt)

        # setting properties to the rate line edit
        self.years.setGeometry(200, 150, 180, 40)
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFont(QFont("Times", 9))

        # creating a loan amount label
        a_label = QLabel("Amount", self)

        # setting properties to the amount label
        a_label.setAlignment(Qt.AlignCenter)
        a_label.setGeometry(20, 200, 170, 40)
        a_label.setStyleSheet(
            "QLabel"
            "{"
            "border : 2px solid black;"
            "background : rgba(70, 70, 70, 35);"
            "}"
        )
        a_label.setFont(QFont("Times", 9))

        # creating a QLineEdit object to get the amount
        self.amount = QLineEdit(self)

        # accepting only number as input
        onlyInt = QIntValidator()
        self.amount.setValidator(onlyInt)

        # setting properties to the rate line edit
        self.amount.setGeometry(200, 200, 180, 40)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFont(QFont("Times", 9))

        # creating a push button
        calculate = QPushButton("Compute Payment", self)

        # setting geometry to the push button
        calculate.setGeometry(125, 270, 150, 40)

        # adding action to the calculate button
        calculate.clicked.connect(self.calculate_action)

        # creating a label to show monthly payment
        self.m_payment = QLabel(self)

        # setting properties to m payment label
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setGeometry(50, 340, 300, 60)
        self.m_payment.setStyleSheet(
            "QLabel" "{" "border : 3px solid black;" "background : white;" "}"
        )
        self.m_payment.setFont(QFont("Arial", 11))

        # creating a label to show monthly payment
        self.y_payment = QLabel(self)

        # setting properties to y payment label
        self.y_payment.setAlignment(Qt.AlignCenter)
        self.y_payment.setGeometry(50, 410, 300, 60)
        self.y_payment.setStyleSheet(
            "QLabel" "{" "border : 3px solid black;" "background : white;" "}"
        )
        self.y_payment.setFont(QFont("Arial", 11))

    # method for calculating monthly
    # and annually payments
    def calculate_action(self):

        # getting annual interest rate
        annualInterestRate = self.rate.text()

        # if there is no number is entered
        if len(annualInterestRate) == 0 or annualInterestRate == "0":
            return

        # getting number of years
        numberOfYears = self.years.text()

        # if there is no number is entered
        if len(numberOfYears) == 0 or numberOfYears == "0":
            return

        # getting loan amount
        loanAmount = self.amount.text()

        # if there is no number is entered
        if len(loanAmount) == 0 or loanAmount == "0":
            return

        # converting text to int
        annualInterestRate = int(annualInterestRate)
        numberOfYears = int(numberOfYears)
        loanAmount = int(loanAmount)

        # getting monthly interest rate
        monthlyInterestRate = annualInterestRate / 1200

        # calculating monthly payemnt
        monthlyPayment = (
            loanAmount
            * monthlyInterestRate
            / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        )

        # setting formatting
        monthlyPayment = "{:.2f}".format(monthlyPayment)

        # setting text to the label
        self.m_payment.setText("Monthly Payment : " + str(monthlyPayment))

        # getting total payment
        totalPayment = float(monthlyPayment) * 12 * numberOfYears
        totalPayment = "{:.2f}".format(totalPayment)

        # setting text to the label
        self.y_payment.setText("Total Payment : " + str(totalPayment))


def macvsc():
    # vsc in mac
    os.system("open /Applications/Visual\ Studio\ Code.app")


def maceclipse():
    # eclipse in mac
    os.system("open /Applications/Eclipse.app")


def winvsc():
    # vsc in windows
    os.system("code")


def wineclipse():
    # eclipse in windows
    # enter path
    subprocess.Popen("path")


def linvsc():
    # vsc in linux
    subprocess.call("code")


def lineclipse():
    # eclipse in linux
    # enter path
    subprocess.call("path")


def macxcode():
    # xcode in mac
    os.system("open /Applications/Xcode.app")


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


# open xcode in mac
def xcode():
    if platform == "darwin":
        macxcode()


# open loan calculator
def loancalc():
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())


# caller function of vscode
def vsc_caller(query):
    vscode()


# caller function of eclipse
def eclipse_caller(query):
    eclipse()


# caller function of xcode
def xcode_caller(query):
    xcode()


# caller function for loan calculator
def loan_caller(query):
    loancalc()


# dictionary of different words which can be used to call the visual studio code and eclipse app
hash_dict = {
    # dictionary of vscode
    "open vscode": vsc_caller,
    "open visual studio code": vsc_caller,
    "open vsc": vsc_caller,
    "vscode": vsc_caller,
    "visual studio code": vsc_caller,
    "vsc": vsc_caller,
    "start vscode": vsc_caller,
    "start visual studio code": vsc_caller,
    "start vsc": vsc_caller,
    "turn on vscode": vsc_caller,
    "turn on visual studio code": vsc_caller,
    "turn on vsc": vsc_caller,
    # dictionary of eclipse
    "eclipse": eclipse_caller,
    "open eclipse": eclipse_caller,
    "start eclipse": eclipse_caller,
    "turn on eclipse": eclipse_caller,
    # dictionary of xcode
    "xcode": xcode_caller,
    "start xcode": xcode_caller,
    "turn on xcode": xcode_caller,
    "open xcode": xcode_caller,
    # dictionary of loan calculator
    "open loan calculator": loan_caller,
    "open loan calc": loan_caller,
    "open loan calc": loan_caller,
    "loan_calculator": loan_caller,
    "loan_calc": loan_caller,
}

# xcode_caller("open")
# vsc_caller("open")
# eclipse_caller("open")
# loan_caller("open")
