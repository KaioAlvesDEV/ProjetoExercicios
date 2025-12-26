frase = input('Digite uma frase: ').strip().lower()
print(f'Primeira vez que aparece "A": {frase.find('a') + 1}\nÚltima vez que aparece "A": {frase.rfind('a') + 1}')
print(f'Quantidade de vezes que aparece: {frase.count('a')}')
input()