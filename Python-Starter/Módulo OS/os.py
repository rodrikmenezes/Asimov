import os

# Mostra o caminho completo do diretório atual
os.getcwd()
diretorio = os.getcwd()

# Retorna uma lista contendo todos os arquivos de determinada pasta
os.listdir()
os.listdir(diretorio)

# os.chdir() - Troca o diretório atual
actual_dir = os.getcwd()
print(os.getcwd())
os.chdir(actual_dir)

# Cria uma pasta.
os.mkdir()
os.mkdir('Pasta Teste')

# Renomeia um arquivo
os.rename()
os.rename('Pasta Teste', 'Pasta Teste 2')

# Deleta arquivo. Não deleta pastas.
os.remove()
os.remove('teste.txt')

# Deleta uma pasta.
os.rmdir()
os.rmdir('Pasta Teste 2')

# Executa um comando de shell
cmd = 'date'
os.system(cmd)
