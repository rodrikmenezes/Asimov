
# Importar
import os

# Diretório
diretorio = os.getcwd()

# Listar tipos de arquivos dentro da pasta diretório
lista_arquivos = []
for x in os.listdir(diretorio):
    if os.path.isfile(x):
        lista_arquivos.append(x)

# Eliminar py
# lista_extensoes.remove('py')


# Obter extensões 
extensoes = []
for x in lista_arquivos:
    y = x.split(sep='.')[1]
    extensoes.append(y)

# Eliminar duplicados
lista_extensoes = list(set(extensoes))


# Criar pastas com o nome das extensões
for x in lista_extensoes:
    os.mkdir(x)

# Mover arquivos
for x in lista_arquivos: print(x)




