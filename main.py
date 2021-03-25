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
      try:
        shutil.copy(path_image,input_folder)
        image_name = os.path.basename(path_image)

        #MANTER MESMO NOME E ALTERAR EXTEMÇÃO PARA PNG
        new_image_name = image_name.replace('.jpg','.png')
        #CONVERTE IMAGEM PARA PNG
        Image.open(input_folder+image_name).save(input_folder+new_image_name)
        
        #REMOVE A IMAGEM JPG
        try:
          os.remove(input_folder+image_name)
        except:
          sg.Popup('Não foi possivel deletar a imagem!!')
        
        #ATUALIZA IMAGEM
        window["-IMAGE-"].update(input_folder+new_image_name)
        
        arquivos = listar_images()
        window["-FILE LIST-"].update(arquivos)
      except:
        sg.Popup('Ocorreu um erro ao carregar a imagem!!')
    elif path_image.endswith(".png") == True:
      shutil.copy(path_image,input_folder)
      image_name = os.path.basename(path_image)
      try:
        window["-IMAGE-"].update(input_folder+image_name)

        arquivos = listar_images()
        window["-FILE LIST-"].update(arquivos)
      except:
        #CASO A IMAGEM TENHA FORMATO DIFERENTE E TENHA SIDO RENOMEADA
        #CONVERTE IMAGEM PARA PNG PARA EVITAR PARA EVITAR POSSIVEIS ERROS
        Image.open(input_folder+image_name).save(input_folder+image_name)
        window["-IMAGE-"].update(input_folder+image_name)

        arquivos = listar_images()
        window["-FILE LIST-"].update(arquivos)
    else:
      sg.Popup('Ocorreu um erro ao carregar a imagem!!!')

  #ATULIZAR IMAGEM AO SELECIONAR NA LISTBOX
  if event == "-FILE LIST-":
    filename = os.path.join(
      values["-FILE LIST-"][0]
    )
    window["-IMAGE-"].update(filename='input/'+filename)

  if event == sg.WIN_CLOSED or event == 'Quit':
    break

window.close()