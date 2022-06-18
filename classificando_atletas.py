#programa que ira definir em qual classe o atleta se enquadra
#receber idade
#classificar de acordo com idade
from datetime import date
ano_nasc = int(input("Insira seu ano de nascimento: "))
ano = date.today().year
idade = ano - ano_nasc
if idade <= 9:
    print(f"Você é um atleta mirim")
elif idade <= 14:
    print(f"Você é um atleta infantil")
elif idade <= 19:
    print(f"Você é um atleta junior")
elif idade <= 25:
    print(f"Você é um atleta senior")
else:
    print(f"Você é um atleta master")