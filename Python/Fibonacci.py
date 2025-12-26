termos = 15
atual = 0
anterior = 1

for termo in range(0, termos):
    print(atual, end=' -> ')
    atual, anterior = atual + anterior, atual
print("ACABOU")
