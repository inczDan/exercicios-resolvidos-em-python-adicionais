#receber o valor de um produto
#as condições de pagamento irao interferir no preço final
    #condições:
# a vista /dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# em até 2x no cartao: mantém o preço
# 3x ou mais : 20% de juros sob o valor total.

produto = float(input("Insira o valor do produto: R$"))
dinheiro_cheque = produto * 0.90
cartao_avista = produto * 0.95
parcelas = produto * 1.20

print(f'{("=-")*10}lojas Daniels {("=-")*10}')
print(f"O valor do seu produto é: R$ {produto:.2f}")
escolha = int(input("""
[1] - Dinheiro ou Cheque (Ganhe 10% de desconto)
[2]- Cartão a vista (Ganhe 5% de desconto)
[3]- Parcelas de 3x ou mais cobramos juros!
Escolha a forma de pagamento: """))
print(f'{("=-")*10}lojas Daniels {("=-")*10}')

if escolha == 1:
    print(f"O valor inicial do seu produto era R${produto:.2f}, com o desconto em dinheiro/cheque ficou R${dinheiro_cheque:.2f}")
elif escolha == 2:
    print(f"O valor inicial do seu produto era R${produto:.2f}, com o desconto do cartão a vista ficou R${cartao_avista:.2f}")
elif escolha == 3:
    print(f"O valor inicial do seu produto era R${produto:.2f}, com as parcelas, passará a ser R${parcelas:.2f}")
else:
    print("O numero  não faz parte da nossa lista")