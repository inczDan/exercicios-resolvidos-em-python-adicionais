#receber nome e peso de varias pessoas em uma lista
#retornar quantas pessoas foram cadastradas
#retprnar uma listagem com as pessoas mais pesadas
#retornar uma listagem com as pessoas mais leves.
dados = []
principal = []
maior = 0
menor = 0
while True:
    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input("Digite o peso: ")))
    if len(principal) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    principal.append(dados[:])
    dados.clear()
    parada = input("Deseja inserir mais pessoas? [S/N]").upper()
    if parada in 'Nn':
        break

print(f"Foram cadastradas {len(principal):.0f} pessoas")
print(f"A mais pesada tem: {maior} KG")
print(f"A mais leve tem {menor} KG")