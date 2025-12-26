velocidade_km = int(input('Insira uma velocidade em Km: '))
velocidade_limite = 80
custo_multa_por_km = 7

if velocidade_km <= velocidade_limite:
    print('Em uma velocidade dentro dos limites, siga a vida')
else:
    multa = (velocidade_km - velocidade_limite) * custo_multa_por_km
    print(f'Acima da velocidade\nMulta de R${multa},00')

input()
