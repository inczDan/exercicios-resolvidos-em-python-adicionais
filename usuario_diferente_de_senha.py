#pedir entrada de usuario
#pedi entrada de senha
#comparar as duas entradas
# retornar sucesso se forem diferentes
#se iguais, entrar em loop que force ser diferentes

usuario = str(input("Insira o seu usuario: "))
senha = (input("Insira sua senha: "))
if usuario != senha:
    print(f"Login com sucesso, {usuario}")
elif usuario == senha:
    print(f"Seu usuario não pode ser igual sua senha")
    while usuario == senha:
        print("Tente novamente")
        usuario = str(input("Insira o seu usuario: "))
        senha = (input("Insira sua senha: "))
        if usuario != senha:
            print(f"Login com sucesso, {usuario}")
