#ler largura em metros
#ler altura em metros
#calcule a area (base * altura)
#dê a quantidade de tinta necessaria sabendo que 1l pinta 2m²
import math
largura = float(input("Coloque a largura em metros: "))
altura = float(input("Coloque a altura em metros: "))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensao de {largura} X {altura} e a area é de: {area}m².')
print(f'Para pintar toda essa area sera necessario: {tinta:.1f}L de tinta')
