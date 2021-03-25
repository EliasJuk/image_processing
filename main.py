from start import *
import PySimpleGUI as sg
import shutil
import os
from PIL import Image

# Layout
first_column = [
  [sg.Input(disabled=True, enable_events=True, key='-FOLDER-', size=(32,1)), sg.FileBrowse()],
  [sg.Listbox(values=fnames, enable_events=True, size=(40, 20), key="-FILE LIST-")]
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
  if event == '-FOLDER-':
    path_image = values['-FOLDER-']

    if path_image.endswith(".jpg") == True:
      #COPIA IMAGEM PARA INPUT
      shutil.copy(path_image,input_folder)
      
      #LISTA ARQUIVOS NA PASTA INPUT
      folder_file = os.listdir('input')

      #RENOMEAR TODAS IMGENS COM A EXTENÇÃO JPG
      for x in folder_file:
        if x.endswith(".jpg") == True:
          #NOVO NOME PARA IMAGEM
          file_paht_name = (input_folder+x)
          converted_image_name = file_paht_name.replace('.jpg','.png')
          try:
            #RENOMEIA A IMAGEM
            os.rename(file_paht_name,converted_image_name)
            image_name = os.path.basename(converted_image_name)
          except:
            #REMOVE IMAGEM CASO JÀ EXISTA UMA COM MESMO NOME
            os.remove(converted_image_name)
            os.rename(file_paht_name,converted_image_name)
            image_name = os.path.basename(converted_image_name)
    else:
      shutil.copy(path_image,input_folder)
      image_name = os.path.basename(path_image)

  if event == sg.WIN_CLOSED or event == 'Quit':
    break

window.close()