#criar tabuada de 1 a 10 utilizando laço for
number_user = int(input("Insira o numero que deseja ver a tabuada: "))
for i in range(1, 11):
    resultado = number_user * i
    print(f"{number_user} X {i} = {resultado}")