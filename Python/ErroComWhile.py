while True:
    sexo = input('Qual seu sexo? ').lower().strip()
    if str(sexo) in ['m', 'f', 'masculino', 'feminino', 'masc', 'fem']:
        break
    else:
        print('Sexo inválido')
