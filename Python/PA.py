while True:
    try:
        tot = int(input('Qual o valor inicial? '))
        r = int(input('Qual a razão? '))
        qtd_termos = int(input('Qual a quantidade de termos? '))
        break
    except ValueError:
        print('APENAS NÚMEROS INTEIROS! TENTE NOVAMENTE')

while qtd_termos > 0:
    for i in range(0, qtd_termos):
        print(tot, end=' -> ')
        tot += r
        qtd_termos -= 1
    print('PAUSA')
    while True:
        try:
            qtd_termos = int(input('Quer mostrar mais quantos termos? '))
            break
        except ValueError:
            print('APENAS NÚMEROS INTEIROS!')
print('ACABOU')
