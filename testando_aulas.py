#teste com dicionario
# dicionario = {'e':1, 'n':1, 'o':1, 'z':1, 'r':1}
# print(dicionario['z'])
#
# resultado = {}
# for caracter in dicionario:
#     contagem = resultado.get (caracter, 0)
#     contagem+=1
#     print("\n", caracter,end=' ')
#     print(contagem,end='')


#criando uma função que retorna numeros em forma de triangulo
# def triangulos_crescentes(n: int):
#     for linha in range(1, n+1):
#         for coluna in range(1, linha+1):
#             print(coluna,end='  ')
#         print('')
# print('triangulo com 1')
# triangulos_crescentes(1)
# print('triangulo com 2')
# triangulos_crescentes(2)
# print('triangulo com 3')
# triangulos_crescentes(10)


    #leetcode
    #urionlinejudge

# """
#
#     >>> numeros_extensos(3)
#     tres
#      >>> numeros_extensos(2)
#      dois
# """
# def numeros_extensos(n1: int):
#     numeros_extensos = {0: 'zero', 1: 'um', 2: 'dois', 3:'tres'}
#     # number_user = int(input("Digite seu numero: "))
#     number_user = n1
#     if number_user in numeros_extensos:
#         print(numeros_extensos[number_user])

# pessoas = []
# dados = ['pedro', 25]
# receitas = ['bolo', 3]
# pessoas.append(dados)
# pessoas.append(receitas)
# galera = list()
# galera.append(pessoas[:])
# dados[0] = 'maria'
# galera.append(pessoas[:])
# print(galera[0][0])

#
# print(dicionario.values())
# print(dicionario.keys())
# print(dicionario.items())
#
# for v, k in dicionario.items():
#     print(f"O {v} e {k}")

# dicionario = {'glorinha': 30, 'ferdnand':450, 20:'arroz'}
# filmes = {'avengers': 2013, 'star Wars': 1977, 'matrix': 1999}
# bolos = {'chocolate': 36.90, 'beijinho': 54.93, 'maracuja': 33.47}
#
#
# lista_aleatoria = []
# lista_aleatoria.append(dicionario)
# lista_aleatoria.append(filmes)
# lista_aleatoria.append(bolos)
# print(f"O filme escolhido nasceu em: {lista_aleatoria[1]['star Wars']}")

# pessoa = {}
# dados = []
# for i in range(0, 3):
#     pessoa['nome'] = str(input(" Digite o nome: "))
#     pessoa['peso'] = int(input("Digite seu peso: "))
#     dados.append(pessoa.copy())
# for n in dados:
#     for v in n.values():
#         print(f" {v}")

# alunos = {}
# for i in range(0, 1):
#     alunos['nome'] = str(input("Digite o nome: "))
#     alunos['media'] = float(input("Digite a media: "))
# print(f"Nome aluno é {alunos['nome']}")
# print(f"Media do aluno é: {alunos['media']}")
# if alunos['media'] <=6:
#     print(f"A situação do(a) aluno(a) {alunos['nome']} é Reprovado(a)")
# else:
#     print(f"A situação do(a) aluno(a) {alunos['nome']} é Aprovado(a)")

# EXEMPLO DE DEFINIÇÃO DE FUNÇÃO E SUA EXECUÇÃO
# def mostralinha():
#     print('-'*10)
# mostralinha()
# print("sistema de alunos")
# mostralinha()
# print("cadastro de funcionarios")
# mostralinha()

# def mensagem(msg):
#     print('-' * 20)
#     print(msg)
#
#
#
# mensagem('olá mundo')
# mensagem('vamos lá')
# mensagem('nao entendi')
#
# def soma(a, b):
#     s = a+b
#     print(s)
#
# soma(10, 5)
# soma(1, 8)
# soma(39, 2)

# def dobra(lst):
#     print(lst) # a lista valores é a mesma coisa que lst
    # pos = 0
    # while pos < len(lst):
    #     lst[pos]*=2
    #     pos+=1
#
# valores = [1, 5, 6, 10]
# dobra(valores)
# print(valores)

# def soma(*num): #a função soma está condizendo com os valores la de baixo do codigo (soma)
#     # # *num é um pacote pois a def soma nao contem parametros identicos, algumas contem 2, outras 3
#     s = 0
#     for n in num:
#         s += n
#     print(s)
#
# soma(1, 20, 10)
# soma(15, 19, -8)
# soma(9, 11)
