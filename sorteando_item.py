import random
from typing import List, Union, Any

nomes = ['Ana Carolina', 'Ana Clara', 'Beatriz R', 'Breno', 'Bruna A', 'Cainã', 'Caio', 'Clara S', 'Daniel A', 'Daniel D', 'David', 'Edinaildo', 'Eliel', 'Evandro', 'fabricio', 'Felipe', 'Fernanda', 'Gabriel', 'Gabriela', 'Gislane', 'Glória', 'Ingrid', 'João', 'Laura', 'Lorrana', 'Lucas M', 'Lucca N', 'Marcela', 'Marcelo', 'Marcos Ornellas', 'marcos viana', 'Marília', 'Rafael', 'Roberto', 'Ronald Perdigão', 'Sara', 'Tábata', 'Victor M', 'Victor Prata']
numeros = list(range(1, 40))

for i in range(1, 40):

        escolhido = random.choice(sorted(nomes))
        cadeira = random.choice(numeros)
        cadeira = random.shuffle(nomes)

        print(f"O aluno escolhido foi {escolhido} e a cadeira é : {cadeira} ")