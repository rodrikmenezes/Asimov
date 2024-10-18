# módulos
import os
import time

# lista carros
carros = {
    
    "1": ["Tracker", 120],
    "2": ["Onix", 90],
    "3": ["Spin", 150],
    "4": ["HB20", 85],
    "5": ["Tucson", 120],
    "6": ["Uno", 60]

}

# lista carros alugados
alugados = {}

# histórico
historico = {}

# contador historico
n = 1

# total
total = 0

# inicio loop
while True:
    
    # limpar tela
    os.system("cls")
    
    # texto inicial
    print("="*10)
    print("[BEM VINDO]")
    print("="*10)
    print("O que deseja fazer?\n")
    print("1: Mostrar Portfólio\n2: Alugar carro\n3: Devolver carro")
    
    # respota inicial
    r = int(input())
    
    # limpar tela
    os.system("cls")
    
    # mostrar portfólio
    if r == 1:
        
        # texto incial
        print("="*10)
        print("[PORTIFÓLIO]")
        print("="*10)
        
        # print portifólio
        for carro in carros.items():
            print("[{}] {} - R$ {}/dia".format(carro[0], carro[1][0], carro[1][1]))
        
        # resposta
        r = int(input("\n1: CONTINUAR?\n2: FIM\n"))
        
        # ação
        if r == 1: 
            pass
        else: 
            
            # limpar tela
            os.system("cls")
            
            break 

    # alugar carro
    elif r == 2:
        
        # texto incial
        print("="*10)
        print("[ALUGAR]")
        print("="*10)
        
        # print portifólio
        for carro in carros.items():
            print("[{}] {} - R$ {}/dia".format(carro[0], carro[1][0], carro[1][1]))
        
        # seleção carro
        x = input("\nSelecione o código carro:\n")
        d = int(input("Por quantos dias deseja alugar o carro\n"))

        # cálculo valor
        v = carros[x][1] * d
        
        # limpar tela
        os.system("cls")
        
        # print texto
        print("="*10)
        print("[ALUGAR]")
        print("="*10)
        print("Você selecionou {} por {} dias".format(carros[x][0], d))
        print("O aluguel totaliza R$ {}. Deseja alugar?".format(v))
        
        # continuar
        r = int(input("\n1: SIM\n2: NÃO\n"))
        
        # alugar carro
        if r == 1: 
            
            # adicionar na lista de alugados
            alugados[x] = carros[x]
            
            # gravar histórico
            historico[n] = [carros[x][0], v]
            
            # excluir carro da lista
            carros.pop(x)
            
            # total
            total += v
            
            # contador
            n += 1
            
            # mensagem
            print("Parabens! Você alugou o carro.")
    
    # devolver carro 
    elif r == 3:
        
        # texto incial
        print("="*10)
        print("[DEVOLVER]")
        print("="*10)

        # print alugados
        for carro in alugados.items():
            print("[{}] {} - R$ {}/dia".format(carro[0], carro[1][0], carro[1][1]))
        
        # que carro devolver?
        x = input("\nQual carro será devolvido?\n")
        
        # ajustar listas
        carros[x] = alugados[x]
        carros = dict(sorted(carros.items()))
        alugados.pop(x)

# print histórico
print("="*10)
print("[RESULTADO]")
print("="*10)
for carro in historico.items():
    print("{} alugado por R$ {}".format(carro[1][0], carro[1][1]))
    
# print total
print("\nTotal = {}\n".format(total))
    




