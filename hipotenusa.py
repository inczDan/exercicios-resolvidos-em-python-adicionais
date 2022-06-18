#ler os comprimentos do cateto oposto
#os comprimentos do cateto adjacente
#calcular
#mostrar comprimento da hipotenusa
from math import sqrt
co = float(input("Comprimento cateto oposto: "))
ca = float(input("Comprimento cateto adjacente: "))
hi = sqrt((co ** 2 + ca ** 2))
print(f"A hipotenusa vai medir: {hi:.2f}")