import PySimpleGUI as sg

# Layout
first_column = [
  [sg.Input(key='input_path_image', size=(32,1)), sg.FileBrowse()],
  [sg.Listbox(values=[], size=(40, 20), key="-FILE LIST-")]
]

second_column = [
  [sg.Image(key="-IMAGE-", size=(400,400))]
]

sg.theme('Reddit')
layout = [
  [sg.Column(first_column), sg.Column(second_column)]
]

# Window
window = sg.Window('image_processing', layout)

# Eventos
while True:
  event, values = window.Read()
  if event == sg.WIN_CLOSED or event == 'Quit':
    break