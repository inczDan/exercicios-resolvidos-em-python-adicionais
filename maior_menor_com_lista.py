# ler 5 valores numericos e guarda-los em uma lista
# devolver o maior
# o menor
# suas posições na lista

lista_do_user = []
maior = 0
menor = 99

for n in range(1, 6):
    numeros = int(input(f"Insira seu {n} numero: "))
    lista_do_user.append(numeros)
    n += 1
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
print(f"O maior numero é {maior} e está na posição {lista_do_user.index(maior)} da lista")
print(f"O menor numero é {menor} e está na posição {lista_do_user.index(menor)} da lista")