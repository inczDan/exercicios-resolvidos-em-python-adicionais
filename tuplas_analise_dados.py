#receber 4 valores int
#emitir quantas vezes o valor 9 aparece
#emitir em que posição está o valor 3
#emitir quais foram os numeros pares.
number_user = ( int(input("Digite o primeiro numero: ")),
                int(input("Digite o segundo: ")),
                int(input("Digite o penultimo: ")),
                int(input("Digite o ultimo: ")))
numeros_do_usuario = number_user
cont = 0
for i in numeros_do_usuario:
    if i == 3:
        print(f"O numero 3 se encontra na posição {numeros_do_usuario.index(3)}")
    if i % 2 == 0:
        print(f"O numero {i} é par")
    if i == 9:
        cont += 1
print(f"O numero 9 aparece {cont} vezes")
