#!//usr/bin/python3

import PySimpleGUIQt as sg
from pynput import keyboard
import subprocess

colorOff='#C5000B'
colorOn='#AECF00'
colorGray='#808080'

stringOff='\n  OFF  \n'
stringOn='\n  ON     \n'

isPressed = 0

def setColors(onOff):
    options = {}
    global stringOff
    global stringOn
    if onOff == 'on' :
        # window.BackgroundColor=colorOn
        window['-TEXT-'].update(stringOn)
        window['-TEXT-'].update(background_color=colorOn)
        window['-BUTTON-'].update(button_color=('black',colorOn))
        window.VisibilityChanged()
    else :
        # window.BackgroundColor=colorOff
        window['-TEXT-'].update(stringOff)
        window['-TEXT-'].update(background_color=colorOff)
        window['-BUTTON-'].update(button_color=('black',colorOff))
        window.VisibilityChanged()

         

# What to do when pause is pressed
def on_press(key):
    global isPressed
    if isPressed == 1: return
    try:
        if key == keyboard.Key.pause:
            setColors('on')
            isPressed=1
            unmuteAll()
    except AttributeError:
        print('something went wrong')

# What to do when pause is released
def on_release(key):
    global isPressed
    try:
        if key == keyboard.Key.pause:
            setColors('off')
            isPressed = 0
            muteAll()
    except AttributeError:
        print('something went wrong')

# Here's a non-blocking listener
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

layout = [
    [sg.Text(stringOff, background_color=colorOff, key='-TEXT-')],
    [sg.Button("Quit", button_color=('black',colorOff), key='-BUTTON-')] ]

# Create the window
window = sg.Window("Mic", layout,
                   background_color=colorGray,
                   keep_on_top=True)

# window.BackgroundColor=colorOn
# window['-TEXT-'].Update(background_color=colorOff)

# window.Element('_TEXT_').Text='On Or OFF'
#window['_TEXT_'].Update()
# window.Element('ciao').Update('pippo')
# window['-TEXT-'].update('My new text value')
# window.Update()

def unmuteAll():
  print("You pressed the SPEAK key")
  subprocess.run("./switchOn.sh")

def muteAll():
  print("You released the SPEAK key")
  subprocess.run("./switchOff.sh")


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "-BUTTON-" or event == sg.WIN_CLOSED:
        break

window.close()
