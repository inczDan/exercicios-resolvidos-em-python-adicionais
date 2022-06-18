#receber tamanho em metros quadrados da area a ser pintada
#tinta cobre 3m quadrado a cada 1 litro
# a tinta é vendida em latas de 18l no valor de 80.00
#retornar ao usuario quantas latas de tinta devem ser compradas
#retornar o total gasto (somente numeros de latas inteiras devem ser vendidas
from math import ceil
area_para_pintar = int(input("Insira a area em metros quadrados: "))
lata_tinta = 54
qnt_latas = 1
litros_necessarios = area_para_pintar / 54

if litros_necessarios > 1.0:
    litros_necessarios * qnt_latas
    print(f'A area é {area_para_pintar}², o numero de latas de tinta necessarias são: {ceil(litros_necessarios)}.\nO valor total é {ceil(litros_necessarios)* 80.00 :.2f} ')
else:
    print(f"Apenas {ceil(litros_necessarios)} lata! Com o total de {ceil(litros_necessarios) * 80.00 :.2f}")