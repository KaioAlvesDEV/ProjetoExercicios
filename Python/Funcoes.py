from random import randint
from time import sleep

def area(largura = 0.0, comprimento = 0.0) -> float:
    """Calcula a área de um retângulo."""
    area = largura * comprimento
    return area

def mostra_cabecalho(simbolo: str, titulo: str) -> None:
    """Mostra um cabeçalho formatado."""
    print(simbolo * len(titulo), f"{simbolo * 4}", sep='')
    print(f'  {titulo}  ')
    print(simbolo * len(titulo), f"{simbolo * 4}", sep='')

def maior(* nums) -> float:
    """Retorna o maior número"""
    return max(nums)

def sorteia_num(quantidade: int, inicio: int, fim: int) -> list:
    """Sorteia uma lista de números aleatórios."""
    numeros = []
    print('Números sorteados: ', end='')
    for _ in range(quantidade):
        numeros.append(randint(inicio, fim))
        print(numeros[-1], end=' ', flush=True)
        sleep(0.5)
    return numeros

def soma_par(* nums) -> int:
    """Soma apenas os números pares."""
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
    return soma

print(area())
nums = sorteia_num(5, 1, 10)
print('\n', soma_par(*nums))
mostra_cabecalho('~', 'Cálculo de Área')
area1 = area(5, 0)
area2 = area(7, 3)
area3 = area(4, 4)

print(f'A área de um terreno de 5m x 10m é de {area1}m².')
print(f'A área de um terreno de 7m x 3m é de {area2}m².')
print(f'A área de um terreno de 4m x 4m é de {area3}m².')

maior_area = maior(area1, area2, area3)
print(f'A maior area calculada foi de {maior_area}m².')
