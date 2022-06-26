#gerar um algoritmo que jogue 4 dados individualmente e sozinho
#listar quanto cada dado retornou de valor dentro de um dict
#fzr um ranking através da organização desse dicionario em forma decrescente

# from random import randint
# from time import sleep
# dados = {}
# lista_resultados = []
# for i in range(1, 5):
#     dados['nome'] = (f'jogador{i}')
#     dados['numero'] = randint(1,6)
#     print(f"O {dados['nome']} tirou {dados['numero']}")
#     sleep(0.7)
#     lista_resultados.append(dados.copy())
# print("O ranking dos jogadores:")
# sleep(0.5)
# print(f"""
# 1° Lugar: {lista_resultados[0]['nome']} com {lista_resultados[0]['numero']}
# 2° Lugar: {lista_resultados[1]['nome']} com {lista_resultados[1]['numero']}
# 3° Lugar: {lista_resultados[2]['nome']} com {lista_resultados[2]['numero']}
# 4° Lugar: {lista_resultados[3]['nome']} com {lista_resultados[3]['numero']}""")
#       PRIMEIRA TENTATIVA SOZIN, SÓ FALTOU CONSEGUIR ORGANIZAR O DICT

from random import randint
from time import sleep
from operator import itemgetter #o sorted nao organiza dicionarios entao temos que importar este modulo
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}
print("Valores sorteados")
for k, v in jogo.items(): #k de keys e v de values que estao passando por cada items do dict
    print(f"O {k} tirou {v} no dado")
    sleep(0.7)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # o itemgetter consegue direcionar o sorted, entao ele funciona se
# passarmos ele no indice de valor numerico. o reverse=true ta sendo responsavel por colocar o ranking em ordem
print("O ranking dos jogadores:")
for i, v in enumerate(ranking): # for com enumerate para numerar cada passagem de i. v[0] passa pela lista de nomes, v[1] pelos resultados dos dados
    print(f"\n{i+1}° lugar: {v[0]} com {v[1]} valores")
    sleep(0.5)
