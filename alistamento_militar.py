#receber o ano de nascimento
# considerar o alistamento aos 18 anos
#informar se é hora de se alistar ou se já passou do tempo
#mostrar o tempo que falta ou o quanto já passou do prazo
from datetime import date

ano_nasc = int(input("Insira seu ano de nascimento: "))
ano_atual = date.today().year
idade_atual = ano_atual - ano_nasc

if ano_atual - ano_nasc > 18:
    print(f"Voce possui {idade_atual}, já se passaram {idade_atual - 18} ano(s) do ano de seu alistamento!")
elif ano_atual - ano_nasc < 18:
    print(f"Voce possui {idade_atual}, ainda resta {18 - idade_atual} ano(s) para se alistar!")
else:
    print(f"Chegou sua vez de se alistar, venha se tornar um braço forte, mão amiga!")
