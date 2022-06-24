"""
Exercício 09 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.

    >>> validar_cpf('734.289.251-30')
    True

    >>> validar_cpf('732.289.294-10')
    False
"""


def validar_cpf(cpf):
    """Escreva aqui em baixo a sua solução"""

def numerar_cpf():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)

def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        #print(f"O CPF digitado é invalido pois nele há {len(cpf)} digitos, o correto é 11")
        return False
    else:
        return True

def primeiro_digito():
    if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
        return False
    else:
        acumulador = 0  #acumulando o resultado #5
        resultado = 0 #3
        controlador = 10 #1
        for numeros in cpf_numerado[0:9]: #2
            resultado = numeros * controlador #multiplica os valores
            acumulador += resultado
            controlador = controlador - 1 #diminui 1 do controlador
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        if acumulador == cpf_numerado[9]:
            return True
        else:
            return False


def segundo_digito():
    acumulador2 = 0  # acumulando o result
    resultado2 = 0
    controlador2 = 11
    for numeros2 in cpf_numerado[0:10]:
        resultado2 = numeros2 * controlador2  # multiplica os valores
        acumulador2 += resultado2
        controlador2 = controlador2 - 1  # diminui 1 do controlador
    acumulador2 = acumulador2 * 10 % 11
    if acumulador2 == 10:
        acumulador2 = 0
    if acumulador2 == cpf_numerado[10]:
        return True
    else:
        return False

cpf_numerado = []
# transforma digitos com ponto em vazio
cpf = str(input("Digite seu cpf: ")).replace('.', '').replace('-', '')

numerar_cpf()
#print(cpf_numerado)
quantidade()

primeiro_digito()

segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("O CPF é valido")
else:
    print("O CPF é invalido")