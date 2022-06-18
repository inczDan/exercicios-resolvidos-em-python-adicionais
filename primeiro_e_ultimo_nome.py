# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro
# e o último nome separadamente.
nome = str(input("Digite seu nome: ")).lower()
nomesplit = nome.split()
ultimo_n = nome.rsplit()
#print(nomesplit)
print(f"Olá {nome}")
print(f"Seu primeiro nome é {nomesplit[0]}")
print(f"E seu ultimo nome é {ultimo_n[len(nomesplit)-1]}")
