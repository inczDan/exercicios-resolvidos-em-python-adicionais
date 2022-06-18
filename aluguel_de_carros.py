#perguntar a quantidade de km percorrido
#quantidade de dias alugados
#dia = 60.00
#km = 0.15
dias_alugados = int(input("Quantos dias de aluguel? (em numero): "))
kms_rodados = float(input("Quantos kms foram rodados? (em numero): "))
dia = 60.00
km = 0.15

custo_dia = dias_alugados * dia
custo_km = kms_rodados * km
print(f"Você usou o carro por {dias_alugados} dias, e rodou {kms_rodados}km's ")
print(f"O custo dos dias alugados é R${custo_dia:.2f}, e dos km's é R${custo_km:.2f}, com o total de R${custo_km + custo_dia:.2f} ")