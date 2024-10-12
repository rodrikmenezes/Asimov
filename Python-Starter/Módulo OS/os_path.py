import os

diretorio = os.getcwd()

# Agrega uma pasta a um caminho. Retorna uma string
novo_diretorio = os.path.join(diretorio, 'Pasta Exemplo')

# Retorna o nome da pasta final de um caminho completo.
os.path.basename(novo_diretorio)
pasta = os.path.basename(novo_diretorio)

# Separa caminho da pasta. Retorna ambos segregados.
os.path.split()
os.path.split(os.getcwd())
split_diretorio = os.path.split(novo_diretorio)

# Retorna a raiz do diretório especificado.
base = os.path.dirname(novo_diretorio)

# Print diretório base e nome da pasta
print('Base: {} \nPasta: {}'.format(base, pasta))

# Retorna o tempo da última atualização do diretório
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)

# Getatime retorna o tempo do último acesso.
from datetime import datetime
datetime.utcfromtimestamp(lt)

# Pergunta se determinado caminho é um arquivo
os.path.isfile(curr_dir) 

# Pergunta se determinado caminho é uma pasta
os.path.isdir(curr_dir) 

