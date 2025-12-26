from math import sqrt, ceil

num = int(input('Digite um número: '))
primo_msg = 'É primo'
raiz_quadrada_num = ceil(sqrt(num))

if num == 2:
    primo_msg = 'É primo'
elif num % 2 != 0 and num > 1:
    for i in range(3, raiz_quadrada_num + 1, 2):
        if num % i == 0:
            primo_msg = 'Não é primo'
            break
else:
    primo_msg = 'Não é primo'

print(primo_msg)

input()
