#programa para ver se o emprestimo pode ser liberado, conforme salario
#receber o valor da casa
#receber o salario
#receber anos de parcelamento
        #obs
#a prestação nao pode exceder 30% do salario, pois negará o emprestimo.

emprestimo_casa = float(input("Insira o valor da residencia: R$"))
salario_valor = float(input("Insira o valor do salario: R$"))
anos_parcelamento = int(input("Em quantos anos pretende parcelar:  "))
maxima_excedencia = 1.30
prestação = anos_parcelamento *12
# o valor do emprestimo dividido pelos anos (mensalidade) nao pode ser
#maior que 30% do salario.

if emprestimo_casa / prestação < 0.30* salario_valor:
    print(f"Muito bem, seu emprestimo no valor de R${emprestimo_casa:.2f} foi aprovado, com pagamento total em {prestação} meses. O valor da parcela é de R${emprestimo_casa/prestação:.2f}!")
else:
    print(f"Seu emprestimo foi negado pois ele superou 30% do seu salario!")