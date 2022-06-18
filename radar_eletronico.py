#ler a velocidade de um carro
#acima de 80km condicoes de multa
#cada km acima da maxima custa 7.00

velocidade_usuario = int(input("Qual velocidade do veiculo: "))
velocidade_max = 80
multa = 7.00
excedeu = 0
if velocidade_usuario <= velocidade_max:
    print(f"Muito bem, sua velocidade é {velocidade_usuario}KM/H continue respeitando as regras!")
elif velocidade_usuario > velocidade_max:
    excedeu = velocidade_usuario - velocidade_max
    total_multa = excedeu * multa
    print(f"IUIUIU, OLHA A MULTA MEU PARCEIRO!!!\n Sua velocidade é {velocidade_usuario}KM/H, a maxima da via é {velocidade_max}KM/H, sua multa ficou no valor de R${excedeu:.2f}")
print("Dirija com segurança")