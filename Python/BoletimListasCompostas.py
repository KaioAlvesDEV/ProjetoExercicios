# BETA v1.0 - Boletim com Listas Compostas

sair = False
alunos_e_notas = [] # Lista para armazenar nomes dos alunos e suas notas

# Loop para adicionar alunos e suas notas
while True:

    nome_aluno = input('Digite o nome do aluno: ').title().strip()
    notas_aluno = [] # Lista para armazenar as duas notas do aluno

    # Coletar as duas notas do aluno
    for i in range(0, 2):

        notas_aluno.append(float(input(f'Digite a {i + 1}ª nota de {nome_aluno} (999 para parar): ')))

        # Verificar se o usuário deseja parar a entrada de notas
        if notas_aluno[i] == 999:

            del nome_aluno            
            del notas_aluno
            sair = True
            break

    if sair:
        break

    alunos_e_notas.append([nome_aluno, notas_aluno])

print(alunos_e_notas)
