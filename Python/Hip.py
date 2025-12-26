from math import hypot

cat1 = float(input('Qual o primeiro cateto? '))
cat2 = float(input('Qual o segundo cateto? '))
hipotetenusa = hypot(cat1, cat2)

print(f'A hipotenusa tem {hipotetenusa:.2f}m²!')

input()