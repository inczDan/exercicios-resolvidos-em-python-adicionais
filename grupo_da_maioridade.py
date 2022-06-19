#algoritmo que leia o ano de nascimento de 7 pessoas
#defina quantas são maiores de 18
#defina quantas são menores de 18
#se 18, considerar maior de idade!
import datetime
ano_atual = datetime.date.today().year
contador_maior = 0
contador_menor = 0
for data in range(1, 8):
    anos = int(input(f"Insira a {data} data de nascimento: "))
    if ano_atual - anos <=17:
        contador_maior += 1
    else:
        contador_menor += 1
print(f"Das 7 entrada, {contador_maior} foram MENORES!",end=' ')
print(f"E {contador_menor} foram MAIORES de idade!")