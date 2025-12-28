aluno = {'Nome': input('Nome do aluno: '),
         'Notas': [float(input('Nota 1: ')), float(input('Nota 2: '))],
         'Media': None,
         'Status': None}

aluno['Media'] = sum(aluno['Notas']) / 2
aluno['Status'] = 'APROVADO' if aluno['Media'] >= 7 else 'REPROVADO' if aluno['Media'] < 4 else 'PROVA FINAL'

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
