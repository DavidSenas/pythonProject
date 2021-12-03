from time import sleep


def Div():
    print("==="*55)


def Soma():
    Div()
    primeiro = float(input("Informe o primeiro número: "))
    segundo = float(input("Informe o segundo número: "))
    for ponto in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    Div()
    print(f"\033[1;97mO resultado de {primeiro} + {segundo} é  = a {primeiro + segundo}\033[0;0m")


def Subtrair():
    Div()
    primeiro = float(input("Informe o primeiro número: "))
    segundo = float(input("Informe o segundo número: "))
    for time in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    Div()
    print(f"\033[1;97mO resultado de {primeiro} - {segundo} é  = a {primeiro - segundo:}\033[0;0m")


def Multiplica():
    Div()
    primeiro = float(input("Informe o primeiro número: "))
    segundo = float(input("Informe o segundo número: "))
    for time in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    Div()
    print(f"\033[1;97mO resultado de {primeiro} X {segundo} é = a {primeiro * segundo}\033[0;0m")


def Dividir():
    Div()
    primeiro = float(input("Informe o primeiro numero: "))
    segundo = float(input("Informe o segundo numero: "))
    for ponto in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    print(f"\033[1;97mO resultado de {primeiro} / {segundo} = a {primeiro / segundo:.2f}\033[0;0m")


def Razi_quadrada():
    import math
    Div()
    num = float(input("Digite o numero: "))
    raiz = math.sqrt(num)
    for ponto in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    Div()
    print(f"\033[1;97mA raiz  quadrada de {num} é = a  {raiz:.2f}\033[0;0m")


def Porcentagem():
    valor = float(input("Digite o Valor que deseja calcular a porcentagem: "))
    porcento = float(input(f"Digite quantos porcento quer calcular de {valor}: "))
    porcentagem = (porcento * valor) / 100
    for ponto in range(0, 3):
        print(".", end="")
        sleep(1)
    print()
    Div()
    print(f"\033[1;97m{porcento}% de {valor} é = a {porcentagem}\033[0;0m")


while True:
    Div()
    try:
        operacao = int(input('''Calculadora Virtual.
        
[1] Somar.
[2] Subtrair.
[3] Multiplicar.
[4] Dividir. 
[5] Raiz Quadrada.
[6] Calcular Porcentagem.

Informe a operação que deseja executar: '''))

        if operacao < 1 or operacao > 6:
            print()
            print("\033[1;31mOPERAÇÃO INVÁLIDA!\033[0;0m")
            continue
    except:
        print()
        print("\033[1;31mERRO DE DIGITAÇÃO!\033[0;0m")
        continue
    else:
        print()

        break
while True:
    try:
        if operacao == 1:
            Soma()

        if operacao == 2:
            Subtrair()

        if operacao == 3:
            Multiplica()

        if operacao == 4:
            Dividir()

        if operacao == 5:
            Razi_quadrada()

        if operacao == 6:
            Porcentagem()

    except:
        print()
        print("\033[1;31mERRO DE DIGITAÇÃO!\033[0;0m")
        continue
    else:
        break

Div()
print()