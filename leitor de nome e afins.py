#ler o nome completo
#informar com upper
#informar com lower
#contar caracteres
#contar somente primeiro nome

nome = (input("Insira seu nome completo: ")).strip()
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
contagem = len(nome)
contagem_primeiro_nome = len(nome.split()[0])
print(f'Seu nome: {nome}')
print(f'Nome maiusculo: {nome_maiusculo}')
print(f'{nome_minusculo}')
print(f"Possui: {contagem - nome.count(' ')} letras")
print(f'Somente o primeiro nome possui {contagem_primeiro_nome} letras')
