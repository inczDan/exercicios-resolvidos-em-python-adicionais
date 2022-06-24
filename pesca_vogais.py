#criar uma tupla e manipular os resultados trazendo as vogais delas ou uma msg dizendo que nao tem

palavras = ("APRENDER", "PROGRAMA", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
            "MERCADO", "PROGRAMADOR", "FUTURO")
for i in palavras:
    print(f"\nA palavra {i.upper()} contem ",end='')
    for letras in i:
        if letras.lower() in 'aeiou':
            print(letras,end=' ')
