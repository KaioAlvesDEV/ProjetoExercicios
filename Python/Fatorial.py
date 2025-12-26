num = 6
fatorial = num

for multiplicador in range(num - 1, 1, -1):
    fatorial *= multiplicador
if num == 0:
    fatorial = 1

print(fatorial)
