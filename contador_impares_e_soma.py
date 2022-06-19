#elaborar um laço que va de 1 até 500
#todos numeros que forem multiplos de 3 devem ser somados
#emitir soma
#emitir laço percorrido
soma = 0
for i in range(1, 501, 2):
    if i % 3 ==0:
        soma += i
        print(i,end=',')
print(soma)