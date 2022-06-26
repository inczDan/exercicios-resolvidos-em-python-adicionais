#ler nome, ano de nascimento e carteira de trabalho
#cadastrar com idade em um dicionario
# se a ctps for != 0 o dicionario recebera o ano de contratação e salario
#calcular e retornar em quantos anos a pessoa ira se aposentar. considerar 35 anos de contribuição
from time import sleep
from datetime import date
dados = {}
ano_atual = date.today().year
for i in range(0,1):
    dados['nome'] = str(input('Insira seu nome: '))
    dados['ano de nasc'] = int(input("Insira a data de nascimento: "))
    dados['ctps'] = int(input("Insira o numero da CTPS [0 caso nao tenha]: "))
    if dados['ctps'] == 0:
        print("Não possui vinculo")
        break
    else:
        dados['ano de contratacao'] = int(input("Ano que foi contratado: "))
        dados['salario'] = float(input("insira seu salario: "))
        sleep(1)
        print("Carregando...")
        sleep(1)
        print("Só mais um instante...")
        sleep(0.5)
        print(f"Nome: {dados['nome']}")
        sleep(0.5)
        print(f"Idade: {dados['ano de nasc']}")
        sleep(0.5)
        print(f"CTPS: {dados['ctps']}")
        sleep(0.5)
        print(f"O ano de contratação foi: {dados['ano de contratacao']}")
        sleep(0.5)
        print(f"Com o salario de : R${dados['salario']:.2f}")
        contribuição = ano_atual - dados['ano de contratacao']
        necessario = 35
        if contribuição - necessario >= 35:
            print("voce ja devia estar aposentado meo '-' ")
        else:
            print(f"você possui : {contribuição} anos de contribuição, para se aposentar faltam {necessario - contribuição} ")