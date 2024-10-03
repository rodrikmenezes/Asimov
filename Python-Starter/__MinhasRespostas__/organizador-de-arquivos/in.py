
# Importar
import os

# Diretório
diretorio = os.getcwd()

# Listar tipos de arquivos dentro da pasta diretório
lista_arquivos = []
for arquivo in os.listdir(diretorio):
    if os.path.isfile(arquivo):
        lista_arquivos.append(arquivo)

# Eliminar in.py
lista_arquivos_sem_py = [x for x in lista_arquivos if not x.endswith('.py')]

# Obter extensões 
extensoes = []
for x in lista_arquivos_sem_py:
    y = x.split('.')[1]
    extensoes.append(y)

# Eliminar duplicados
extensoes_sem_duplicados = list(set(extensoes))

# Criar pastas com o nome das extensões
for x in extensoes_sem_duplicados: os.mkdir(x)

# Mover arquivos
for x in lista_arquivos_sem_py:
    extensao = x.split('.')[1]
    origem = os.path.join(diretorio, x)
    destino = os.path.join(diretorio, extensao, x)
    os.rename(origem, destino)



