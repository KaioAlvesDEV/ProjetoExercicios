valor = float(input('INSIRA UM VALOR: '))
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0
while valor > 0:
    if valor - 50 >= 0:
        valor -= 50
        cedula50 += 1
    elif valor - 20 >= 0:
        valor -= 20
        cedula20 += 1
    elif valor - 10 >= 0:
        valor -= 10
        cedula10 += 1
    elif valor - 1 >= 0:
        valor -= 1
        cedula1 += 1
    else:
        break
print(f'''{cedula50} Cédulas de 50 reais
{cedula20} Cédulas de 20 reais
{cedula10} Cédulas de 10 reais
{cedula1} Cédulas de 1 real
{valor:.2f} reais perdidos''')
