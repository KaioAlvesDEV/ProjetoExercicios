soma_total = num_usuario = 0
while num_usuario != 999:
    num_usuario = int(input('Digite um número para somar (999 para): '))
    if num_usuario != 999:
        soma_total += num_usuario
print(soma_total)
