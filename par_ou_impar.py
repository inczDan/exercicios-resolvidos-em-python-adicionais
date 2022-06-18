#entrada de dados
#condicao para numero ser impar ou par

numero = int(input("Insira seu numero: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par")
elif numero % 2 != 0:
    print(F"O numero {numero} é impar")