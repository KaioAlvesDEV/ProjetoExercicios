from random import shuffle

alunos = [input('Primeiro aluno: '), input('Segundo aluno: '), input('Terceiro aluno: '), input('Quarto aluno: ')]
shuffle(alunos)

print(f'ORDEM DE APRESENTAÇÃO: {alunos}')

input()
