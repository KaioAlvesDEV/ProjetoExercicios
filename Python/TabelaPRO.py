lista = ('Arroz', 29.90,
         'Feijão', 35.90,
         'Margarina', 4.90,
         'Refrigerante It', 14.90)

for produto in range(0, len(lista), 2):
    num_caracteres = len(lista[produto])
    print(f'{lista[produto]}{lista[produto + 1]:.>{50 - num_caracteres}}0')
