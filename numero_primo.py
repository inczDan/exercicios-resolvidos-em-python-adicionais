#ler um numero int
#retornar msg informando se é primo ou nao
total = 0
number_user = int(input("Insira seu numero: "))
for i in range(1, number_user+1 ):
    if number_user % i ==0:
        total += 1
print(f"Seu numero passou por {i} numeros e foi divisivel por {total} numeros!")
print('caso o numero de divisoes seja maior que 2, não considere um numero primo!')