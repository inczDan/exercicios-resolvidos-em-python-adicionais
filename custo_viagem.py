#receber a distancia da viagem em km
#preco por km de 0.50 para viagem de 200km
#preco por km de 0.45 para viagem acima de 200km
#entregar o valor total

distancia_viagem = float(input("Insira a distancia em km: "))
valor_menor_viagem = 0.50
valor_maior_viagem = 0.45

if distancia_viagem <=200:
    total_curta = valor_menor_viagem * distancia_viagem
    print(f"Sua viagem tem um total de {distancia_viagem} KM's, cada km custará R${valor_menor_viagem:.2f}, e seu total é de: R${total_curta:.2f}")
elif distancia_viagem >200:
    total_longa = valor_maior_viagem * distancia_viagem
    print(f"Sua viagem tem um total de {distancia_viagem} KM's, cada km custará R${valor_maior_viagem:.2f}, e seu total é de: R${total_longa:.2f}")
print("Boa viagem :) ")