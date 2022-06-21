# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

def valida_cpf(cpf: str) -> bool:
    """Função para validação de CPF
Recebe: CPF -> Str
Retorna: True ou False
"""
import re

def calcula_digito(cpf: str, digito_no: int, cont=10) -> int:
    if digito_no == 1:
        fatia = cpf[0:9]
        digito = int(cpf[-2])
    else:
        fatia = cpf[1:10]
        digito = int(cpf[-1])

    calculo = 0
    for i in fatia:
        calculo += int(i) * cont
        cont -= 1
        digito_calculado = round((calculo * 10) % 11, 2)

    # caso o resto seja 10, o digito passa a ser 0
    digito_calculado = round(digito_calculado, 1) if digito_calculado != 10 else 0

    return digito_calculado == digito

    cpfs_invalidos = [
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
    "00000000000",
    ]

    # limpa cpf deixando somente números
    cpf_digitos = "".join(re.findall("\d+", cpf))

    if cpf_digitos in cpfs_invalidos:
        return False

    digito1_verificacao = calcula_digito(cpf_digitos, 1)
    digito2_verificacao = calcula_digito(cpf_digitos, 2)

    return digito1_verificacao and digito2_verificacao