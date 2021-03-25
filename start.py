######################################
########### INICIALIZAÇÃO ############
######################################
import os

#DIRETORIO RAIZ
dir_path = os.getcwd()

#PASTAS INPUT E OUTPUT
input_folder =  dir_path+'/input/'
output_folder = dir_path+'/output/'

#CRIA PASTA INPUT E OUTPUT SE NAO EXISTIR
if os.path.exists(input_folder) == False:
  os.mkdir('input')

if os.path.exists(output_folder) == False:
  os.mkdir('output')

#CRIA PASTA TEMP SE NAO EXISTIR
diretorio_atual = os.getcwd()
if os.path.exists(diretorio_atual+'/input/temp') == False:
  os.mkdir(diretorio_atual+'/input/temp')


######################################
############## FUNCOES ###############
######################################

try:
  file_list = os.listdir('input')
except:
  file_list = []

#FILTRAR POR IMAGENS
fnames = [
  f
  for f in file_list
    if os.path.isfile(os.path.join('input', f))
    and f.lower().endswith((".png", ".jpg"))
]

#LISTA CONTEUDO DA PASTA INPUT
def listar_images():
  try:
    file_list = os.listdir('input')
    fnames = [
    f
    for f in file_list
      if os.path.isfile(os.path.join('input', f))
      and f.lower().endswith((".png", ".jpg"))
    ]
    return fnames
  except:
    file_list = []
    return file_list

#GERA UMA IMAGEM DE TAMANHO REDUZIDO APARTIR DA IMAGEM ORIGINAL
def gerar_miniatura():
    image = Image.open(converted_image_name)
    MAX_SIZE = (400, 400)
    image.thumbnail(MAX_SIZE)
    image.save('input/temp/'+original_image)