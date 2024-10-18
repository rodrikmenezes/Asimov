
# Importar
import os

# Diretório
diretorio = os.getcwd()

# Lista de pastas e arquivos
lista_diretorio = os.listdir(diretorio)

# Lista de pastas dentro do diretorio
lista_pastas = [x for x in lista_diretorio if os.path.isdir(x)]

# Remover arquivos das pastas e deletar pasta
for pasta in lista_pastas:
    pasta_origem = os.path.join(diretorio, pasta)
    lista_arquivos = os.listdir(os.path.join(diretorio, pasta))
    if len(os.listdir(pasta_origem)) != 0:
        for arquivo in lista_arquivos:
            origem = os.path.join(pasta_origem, arquivo)
            destino = os.path.join(diretorio, arquivo)
            os.rename(origem, destino)
        os.rmdir(pasta_origem)


