# módulos
import os
import time

operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "/": "Divisão",
    "*": "Multiplicação",
    "^": "Exponenciação"
}


# iniciar loop
while True:
    os.system("cls")

    # gravar operação
    for i in operacoes.items():
        print("{} : {}".format(i[0], i[1]))
    
    # selecionar operação
    op = input("\nSelecione a operação desejada:\n")
    on = operacoes[op]
    
    # print seleção
    print(f"A operação selecionada foi:\n{on}\n")
    
    # solicitar valores
    x = int(input("Qual o primeiro valor?\n"))
    y = int(input("Qual o segundo valor?\n"))

    # efetuar operação
    if on == "Soma":
        r = x + y
    elif on == "Subtração":
        r = x - y
    elif on == "Divisão":
        r = x / y
    elif on == "Multiplicação":
        r = x * y
    elif on == "Exponenciação":
        r = x ** y
    
    # mostrar resultado
    time.sleep(1)
    print(f"\n{x} {op} {y} = {r}")
    time.sleep(1)
    
    # questinar se usuário deseja continuar
    continuar = int(input("\nDeseja realizar outra operação?\n0: Não\n1: Sim\n"))

    # fim
    if continuar == 0: break

# limpar tela
os.system("cls")
