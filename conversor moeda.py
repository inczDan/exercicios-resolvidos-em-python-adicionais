#converter reais para compra de dolar
# 1 dolar = 5
reais_carteira = float(input("Coloque quantidade de reais: R$ "))
valor_dolar = 5.00
qnt_dolares = reais_carteira / valor_dolar
print(f'A quantidade de dolares possiveis para compra é : US${qnt_dolares}')