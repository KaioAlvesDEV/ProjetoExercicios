valores = [int(input(f'Digite o valor {valor}: ')) for valor in range(1, 6)]

maior = max(valores)
menor = min(valores)

posicoes_maior = [i + 1 for i, n in enumerate(valores) if n == maior]
posicoes_menor = [i + 1 for i, n in enumerate(valores) if n == menor]

print(f'O maior valor foi o número {maior} na(s) posição(s): {posicoes_maior}')
print(f'O menor valor foi o número {menor} na(s) posição(s): {posicoes_menor}')
