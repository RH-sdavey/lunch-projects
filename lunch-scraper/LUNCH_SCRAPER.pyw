#!/usr/bin/python3
from subprocess import call
import PySimpleGUI as sg
import shutil
import time
import webbrowser

CREATE_NO_WINDOW = 0x08000000

all_btn_color = ('white', 'blue')
sg.ChangeLookAndFeel('Dark')

def outputText(text):
    if str(text).startswith("setting up"):
        print("setting up template file..", end=" ")
        window.Refresh()
        time.sleep(1)
    elif str(text).startswith("Done"):
        print("..Done.")
        window.Refresh()
    elif str(text).startswith("Error"):
        print("..Error..    ")
        window.Refresh()
    else:
        print("Scraping {}".format(text), end=" ")
        window.Refresh()

def button_obed():
    outputText("setting up")
    shutil.copy('indexBACKUP.html', 'index.html')
    outputText("Done")
    outputText("Miomi Sushi")
    outputText("Done")
    outputText("Tesare")
    outputText("Done")
    outputText("IQ Restaurant")
    outputText("Done")
    outputText("Basta")
    call(["python", "basta.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Pupek")
    call(["python", "pupek.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Makalu")
    call(["python", "makalu.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("StaroBrno Brewery")
    outputText("Done")
    outputText("Gingilla")
    call(["python", "gingilla.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Union")
    call(["python", "union.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Kometa Arena")
    outputText("Done")
    outputText("Babeta")
    call(["python", "babeta.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Sediveho Vola")
    call(["python", "sediveho.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Zelezna Ruze")
    outputText("Done")
    outputText("Mitrovski")
    call(["python", "mitrovski.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Tanuki")
    call(["python", "tanuki.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Dr Indy")
    call(["python", "drindy.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Coloseum")
    call(["python", "coloseum.py"], creationflags=CREATE_NO_WINDOW)
    outputText("Done")
    outputText("Eurest")
    outputText("Done")
    outputText("Adding a few delivery links...")
    outputText("Done")
    outputText("Opening Web browser and closing this dialogue box. See you! ")
    time.sleep(2)
    webbrowser.open("index.html", autoraise=True)
    quit()

dispatch_dictionary = {'Scrape Lunches': button_obed}

buttonCol = [
    [sg.Button('Scrape Lunches', button_color=all_btn_color, size=(65,5))],
    [sg.VerticalSeparator()],
]

textCol = [
    [sg.Output(size=(80, 90))]
]
quitcol = [
    [sg.Quit(size=(60,20))]
]

layout = [
    [sg.Column(buttonCol, background_color='LightGrey', size=(500, 80))],
    [sg.Column(textCol, background_color='LightGrey', size=(500, 400))],
    [sg.Column(quitcol, background_color='LightGrey')],
]

# Show the Window to the user
window = sg.Window('Sean Lunch Scraper', layout, finalize=True, background_color='LightGrey', button_color=all_btn_color, size=(600, 600))

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', None):
        break
    # Lookup event in dispatch_dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()
