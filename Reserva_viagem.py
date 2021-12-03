def Div():
    print("\033[1;97m")
    print("---"*50)
    print("\033[0;0m")


def SaldoViagem(reserva, gasto_dia):
    from time import sleep
    SaldoConta = reserva
    GastoDiario = gasto_dia
    TotDia = 0
    while True:
        if SaldoConta > GastoDiario or GastoDiario - SaldoConta == 0:
            SaldoConta -= GastoDiario
            TotDia += 1
        else:
            print("Aguarde um instante, estamos calculando.")
            break
    for c in range(0, 10):
        print("-", end="")
        sleep(0.45)
    print()
    print(f"\033[1;97mSaldo inicial R$ {reserva}")
    print(f"Gasto programado por dia de R$ {gasto_dia:.2f}")
    print(f"Duração de {TotDia} Dias.")
    print(f"Saldo final R$ {SaldoConta:.2f}.")


Div()
print("\033[1;34mIremos te ajudar a programar suas viagens de modo bem simples, basta seguir as orientações a baixo.")
print()
while True:
    try:
        Div()
        Valor_Conta = float(input("Informe o valor de sua reserva finaceira separada para viagem: "))
        desp_diária = float(input("Informe o Valor que pretende Gastar diariamente na viagem: "))
        Div()
        SaldoViagem(Valor_Conta, desp_diária)
        Div()
    except:
        print("\033[1;31mERRO INESPERADO")
        continue

    else:
        print()
    break

