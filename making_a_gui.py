# https://realpython.com/courses/simplify-gui-dev-pysimplegui/
# https://www.youtube.com/watch?v=-_z2RPAH0Qk
# https://github.com/PySimpleGUI/PySimpleGUI

# VENV --> source pysimplegui/bin/activate

# pip install pysimplegui

# import PySimpleGUI as sg



sg.Window(title="Hello World", layout=[[sg.Text("Hello 1")]], margins=(100,50)).read()

sg.Window(title="Hello World", layout=[[sg.Text("Hello 2")]], margins=(100,50)).read()

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

# Create the Window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()



# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()