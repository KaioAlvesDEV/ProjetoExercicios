from datetime import date

ano_user = int(input('Digite um ano qualquer: '))

 #0 no ano significa que o usuário quer o ano atual
if ano_user == 0:
    ano_user = date.today().year

#Calculo de ano bissexto
eh_ano_bissexto = ano_user % 4 == 0 and ano_user % 100 != 0 or ano_user % 100 == 0 and ano_user % 400 == 0

if eh_ano_bissexto:
    print(f'{ano_user} é ano bissexto')
else:
    print(f'{ano_user} não é ano bissexto')

input()
