#!/usr/bin/python
# pystretch.py

import os
import PySimpleGUI as sg

layout = [[sg.Text("Edit the config file before using!", background_color='#2b2b2b')], [sg.Button('STRETCH', button_color = "#000000")], [sg.Button('UNSTRETCH', button_color = "#000000")]]

# Create the window
window = sg.Window("pystretch", layout, background_color='#2b2b2b')

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    # presses STRETCH will stretch resolution & presses UNSTRETCH will unstretch resolution
    if event == "STRETCH":
        os.system('./stretch.sh')
    if event == "UNSTRETCH":
        os.system('./unstretch.sh')
    if event == sg.WIN_CLOSED:
        break

window.close()