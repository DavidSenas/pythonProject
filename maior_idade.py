from datetime import date
from time import sleep

data = date.today().year
linha = ("==="*55)
print(linha)
print()
print("Precisamos Fazer algumas confirmações antes de liberar o acesso.")
print()
print(linha)
while True:
    try:
        anostr = str(input("Informe o ano de seu nascimento composto pelos 4 digitos: "))
        if len(anostr) < 4 or len(anostr) > 4:
            print("\033[1;31mERRO, DIGITE OS 4 DIGITOS DO ANO DO SEU NASCIMENTO!\033[0;0m")
            continue
        else:
            ano = int(str(anostr))
        print('Aguarde, Estamos verificando autorização de acesso!')
        sleep(3)
        idade = data - ano
        if idade < 0 or idade > 130:
            print("\033[1;31mERRO, VERIFIQUE O ANO E TENTE NOVAMMENTE!\033[0;0m")
            print(linha)
            continue
    except:
        print()
        print("\033[1;31mERRO DE DIGITAÇÃO!\033[0;0m")
    else:
        if idade < 18:
            print(linha)
            print(f"\033[1;31mSem Permissão de Acesso.")
            break
        else:
            print(linha)
            print(f"\033[1;32mPermissão de acesso Concedida.")
            break

