# reter nome e media aluno em dict
#retornar nome e media
#retornar mensagem se foi aprovado ou nao

alunos = {}
for i in range(0, 1):
    alunos['nome'] = str(input("Digite o nome: "))
    alunos['media'] = float(input("Digite a media: "))
print(f"Nome aluno é {alunos['nome']}")
print(f"Media do aluno é: {alunos['media']}")
if alunos['media'] <=6:
    print(f"A situação do(a) aluno(a) {alunos['nome']} é Reprovado(a)")
else:
    print(f"A situação do(a) aluno(a) {alunos['nome']} é Aprovado(a)")