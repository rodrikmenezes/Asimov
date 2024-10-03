
# Importar
import os

# Diretório
diretorio = os.getcwd()

# Listar pastas
lista_pastas = []
for x in os.listdir(diretorio):
    if os.path.isdir(x):
        lista_pastas.append(x)

# Remover arquivos das pastas
for pasta in lista_pastas:
    origem = os.path.join(diretorio, pasta)
    lista_arquivos = os.listdir(origem)
    for arquivo in lista_arquivos:
        origem_temp = os.path.join(origem, arquivo)
        destino = os.path.join(diretorio, arquivo)
        os.rename(origem_temp, destino)

# Apagar pastas
for pasta in lista_pastas:
    caminho_completo = os.path.join(diretorio, pasta)
    try:
        os.rmdir(caminho_completo)
    except OSError as e:
        print(f'Erro ao deletar {caminho_completo}: {e}')



