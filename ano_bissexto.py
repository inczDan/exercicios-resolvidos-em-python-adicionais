#receber qualquer ano
#retornar se é bissexto ou nao

ano = int(input("Insira o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto!")
else:
    print(f"O ano {ano} não é Bissexto!!")