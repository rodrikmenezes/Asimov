
# Importar
import os

# Diretório
diretorio = os.getcwd()

# Lista de pastas e arquivos
lista_diretorio = os.listdir(diretorio)

# Lista de arquivos excluindo arquivos .py
lista_arquivos = [x for x in lista_diretorio if os.path.isfile(x) and '.py' not in x]

# Obter extensões 
extensoes = list(set([x.split('.')[1] for x in lista_arquivos]))

# Criar pastas com o nome das extensões
for x in extensoes: os.mkdir(x)

# Mover arquivos
for x in lista_arquivos:
    pasta_destino = x.split('.')[1]
    origem = os.path.join(diretorio, x)
    destino = os.path.join(diretorio, pasta_destino, x)
    os.rename(origem, destino)



