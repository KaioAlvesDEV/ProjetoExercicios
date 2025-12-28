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
        if sair_input in ('S', 'N', 'SIM', 'NÃO'):
            break
        
    alunos_e_notas.append([nome_aluno, notas_aluno])

    # Verificar se o usuário deseja sair do loop principal
    if sair_input in ('S', 'SIM'):
        sair = True
        break

print('===' * 10, ' BOLETIM ', '===' * 10)
print(f'\n{"Nº":<4}{"ALUNO":<30}{"MÉDIA":>8}')

# Exibir a média de cada aluno
for i, aluno in enumerate(alunos_e_notas):
    media_aluno = sum(aluno[1]) / 2
    print(f'{i:<4}{aluno[0]:<30}{media_aluno:>8.2f}')

### TAREFAS HOJE: 
# Exibir média de cada aluno |FEITA|
# Permitir verificar notas de cada aluno individualmente
# Mostrar quem tirou a maior e menor nota
# Mostrar quem reprovou, quem passou e quem vai pra prova final
