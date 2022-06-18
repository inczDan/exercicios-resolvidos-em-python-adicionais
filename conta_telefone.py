#receber os minutos que foram utilizados
        #condicoes
#abaixo de 200 min o preco é 0.20 por min
#entre 200 e 400 min, o preco é 0.18 por min
#acima de 400 min o preço é 0.15 por min

uso_tel = int(input("Qual foi o total de minutos utilizados?: "))
if uso_tel < 200:
    valor_total = uso_tel * 0.20
    print(f"Você utilizou {uso_tel} min, totalizando R${valor_total:.2f}")
elif uso_tel > 200 or uso_tel < 400:
    valor_total = uso_tel * 0.18
    print(f"Você utilizou {uso_tel} min, totalizando R${valor_total:.2f}")
else:
    valor_total = uso_tel * 0.15
    print(f"Você utilizou {uso_tel} min, totalizando R${valor_total:.2f}")