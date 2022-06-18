#ler um nome
#confirmar se é vdd ou false
#retornar resposta
cidades_certas = ['Santos', 'Rio de janeiro'.title(), 'Goias']
cliente = str(input("Digite a cidade certa: ")).title()


if cliente in cidades_certas:
    print("True")
else:
    print('False')
