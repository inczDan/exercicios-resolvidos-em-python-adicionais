#receber valores fixos
#receber valores variaveis
#calcular total de cada um
#calcular total em conjunto
conteudo = 's' or 'n'
while True:
        if conteudo == 's':
            c_fixos = float(input("Digite as contas fixas: "))
            conteudo = str(input("Existem mais valores? ('s' ou 'n'): "))
        elif conteudo == 'n':
            c_variaveis = float(input("Digite as contas variaveis: "))
            conteudo = str(input("Existem mais valores? ('s' ou 'n'): "))

        else:
            conteudo != 's' or conteudo != 'n'
            print("Voce deve inserir 's' ou 'n' ")
            break


            valores_fixos = [c_fixos]
            valores_variaveis = [c_variaveis]
            print(valores_fixos)
            print(valores_variaveis)
