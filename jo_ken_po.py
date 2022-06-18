# receber a entrada do jogador
#estruturar o pensamento do computador
#emitir a resposta com o tempo prolongado para dar mais enfase
#emitir resultado
import random
from time import sleep
escolha_user = int(input("""
[1] - Pedra
[2] - Papel
[3] - Tesoura
Escolha uma opção: """))


lista_pc = ['pedra', 'papel', 'tesoura']
if escolha_user == 1:
    print(f"Vamos lá! você escolheu {lista_pc[0]}")
elif escolha_user == 2:
    print(f"Vamos lá! você escolheu {lista_pc[1]}")
else:
    print(f"Vamos lá! você escolheu {lista_pc[2]}")
print("O computador está escolhendo...")
sleep(1)
print('JÒ')
sleep(0.5)
print("   Ken")
sleep(1)
print("       Pô")
escolha_pc = random.randint(0, 2)
sleep(0.7)
print(f"A escolha do computador foi {(lista_pc[escolha_pc])}")
if escolha_pc == 0:
    if escolha_user == 1:
        print("Vocês empataram!!")
    elif escolha_user == 2:
        print("Você ganhou, papel cobre a pedra!")
    elif escolha_user == 3:
        print("Você Perdeu, tesoura quebra contra a pedra!")
elif escolha_pc == 1:
    if escolha_user == 1:
        print("Você Perdeu, papel cobre a pedra!")
    elif escolha_user == 2:
        print("Vocês empataram!!")
    elif escolha_user == 3:
        print("Você ganhou, tesoura corta o papel!")
elif escolha_pc == 2:
    if escolha_user == 1:
        print("Você ganhou, tesoura quebra contra a pedra!")
    elif escolha_user == 2:
        print("Você Perdeu, tesoura corta o pepel!")
    elif escolha_user == 3:
        print("Vocês empataram!!")