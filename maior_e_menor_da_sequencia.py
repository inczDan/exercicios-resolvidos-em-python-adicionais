#ler o peso de 5 pessoas
#devolver o menor peso
#devolver o maior peso
from math import inf
menor = inf
maior = 0
soma = 0
for i in range(1, 6):
    pesos = float(input(f"Insira o {i}° peso: "))
    if pesos > maior:
        maior = pesos

    if pesos < menor:
        menor = pesos
    soma = maior +menor
print(f"O menor peso recebido foi {menor} e o maior peso foi {maior} e a soma de ambos {soma}")