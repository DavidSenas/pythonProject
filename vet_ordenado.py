from time import sleep


def Div():
    print("---"*50)
print()
print("Ordenando a lista a baixo e Mostrando na tela junto com os números em extenso.")
print([8, 4, 6, 9, 2, 5, 10, 7, 1, 3])
print()
print("\033[1;97mAguarde estamos Trabalhando na lista.\033[0;0m")


for time in range(0,10):
    print("_", end="")
    sleep(0.30)
print()

Div()
vetor = [8, 4, 6, 9, 2, 5, 10, 7, 1, 3]
extenso = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez"]
fundidas = dict(zip(sorted(vetor), extenso))


for keys, values in fundidas.items():
    print(f"{keys:<2} - ({values:^8}) ")
    sleep(1)

Div()
print()

