# BETA v1.0.3 - Boletim com Listas Compostas

sair = False
alunos_e_notas = [] # Lista para armazenar nomes dos alunos e suas notas

# Loop para adicionar alunos e suas notas
while not sair:

    nome_aluno = input('Digite o nome do aluno: ').title().strip()
    notas_aluno = [] # Lista para armazenar as duas notas do aluno

    # Coletar as duas notas do aluno
    for i in range(0, 2):

        notas_aluno.append(float(input(f'Digite a {i + 1}ª nota de {nome_aluno}: ')))
    
    # Perguntar se o usuário deseja sair
    while True:
        sair_input = input('Deseja sair? (S/N): ').upper().strip()
        if sair_input in ('S', 'N', 'SIM', 'NÃO', 'NAO'):
            break
        
    alunos_e_notas.append([nome_aluno, notas_aluno])

    # Verificar se o usuário deseja sair do loop principal
    if sair_input in ('S', 'SIM'):
        sair = True
        break

print('===' * 10, ' BOLETIM ', '===' * 10)
print(f'\n{"Nº":<4}{"ALUNO":<30}{"MÉDIA":>8}')

# Exibir a média de cada aluno
for i, aluno in enumerate(alunos_e_notas, 1):

    media_aluno = sum(aluno[1]) / 2
    print(f'{i:<4}{aluno[0]:<30}{media_aluno:>8.2f}')

sair = False

# Loop para permitir ver as notas de cada aluno individualmente
while True:

    # Perguntar se o usuário deseja ver as notas de algum aluno
    while True:
        ver_notas_input = input('Deseja ver as notas de algum aluno? (S/N): ').upper().strip()

        # Validar entrada do usuário
        if ver_notas_input in ('S', 'N', 'SIM', 'NÃO', 'NAO'):
            if ver_notas_input in ('N', 'NÃO', 'NAO'):
                sair = True
            break

    if sair:
        break

    # Solicitar o número do aluno para ver suas notas
    while True:

        aluno_numero = int(input('Digite o número do aluno que deseja ver as notas: '))
        if 1 <= aluno_numero <= len(alunos_e_notas):
            break
    
    aluno_selecionado = alunos_e_notas[aluno_numero - 1]

    print(f'Notas de {aluno_selecionado[0]}: {aluno_selecionado[1][0]} e {aluno_selecionado[1][1]}')

### TAREFAS HOJE: 
# Exibir média de cada aluno |FEITA|
# Permitir verificar notas de cada aluno individualmente
# Mostrar quem tirou a maior e menor nota
# Mostrar quem reprovou, quem passou e quem vai pra prova final
