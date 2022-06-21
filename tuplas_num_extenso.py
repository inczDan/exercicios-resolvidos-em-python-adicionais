number_user = int(input("Insira um numero de 1 a 8: "))
num_extensos = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito')
if number_user > -1 and number_user < 9 :
    print(f"você digitou {num_extensos[number_user]}")
else:
    while True:
        if number_user < 0 or number_user >= 9:
            number_user = int(input("Insira um numero correto: "))
            print(f"você digitou {num_extensos[number_user]}") # num_extensos recebeu o input do usuario como numero de indice para buscar dentro da tupla (irado)
            break
