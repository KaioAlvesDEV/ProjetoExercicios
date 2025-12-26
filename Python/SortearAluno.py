from random import choice

alunos = [input('Diga o primeiro aluno: '), input('Diga o segundo aluno: '), input('Diga o terceiro aluno: '),
          input('Diga o quarto aluno: ')]

print(f'O aluno sorteado foi {choice(alunos)}!')

input()
