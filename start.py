import os

dir_path = os.getcwd()

input_folder =  dir_path+'/input/'
output_folder = dir_path+'/output/'

if os.path.exists(input_folder) == False:
  os.mkdir('input')

if os.path.exists(output_folder) == False:
  os.mkdir('output')

#CRIA PASTA TEMP SE NAO HOUVER
diretorio_atual = os.getcwd()
if os.path.exists(diretorio_atual+'/input/temp') == False:
  os.mkdir(diretorio_atual+'/input/temp')

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
def listar():
  try:
    file_list = os.listdir('input')
    return file_list
  except:
    file_list = []
    return file_list