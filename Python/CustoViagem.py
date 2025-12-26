distancia_viagem = float(input('Qual a distância da viagem em Km? '))
preco_por_km = 0.5
qtd_km_para_desconto = 200
preco_km_com_desconto = preco_por_km - preco_por_km * 0.1 #O número é a % do desconto

if distancia_viagem <= qtd_km_para_desconto:
    preco_viagem = preco_por_km * distancia_viagem
else:
    preco_viagem = preco_km_com_desconto * distancia_viagem

print(f'PREÇO FINAL: R${preco_viagem:.2f}')

input()
