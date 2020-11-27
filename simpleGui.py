
import PySimpleGUIQt as sg

colorOff='#C5000B'
colorOn='#AECF00'

layout = [[sg.Text("ON/OFF", key='-TEXT-')], [sg.Button("Quit")]]

# Create the window
window = sg.Window("Mic", layout, background_color=colorOff, finalize=True)

window.BackgroundColor=colorOn
# window.Element('_TEXT_').Text='On Or OFF'
#window['_TEXT_'].Update()
# window.Element('ciao').Update('pippo')
# window['-TEXT-'].update('My new text value')
# window.Update()

def pressed():
  print("You pressed the key")



# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()
