
import PySimpleGUIQt as sg

layout = [[sg.Text("Microphone is off")], [sg.Button("Quit")]]

# Create the window
window = sg.Window("Mic", layout, background_color='white')
window.BackgroundColor='black'

# window.TKroot.configure(background=white)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()
