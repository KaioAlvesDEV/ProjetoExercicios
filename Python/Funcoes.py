def area(largura: float, comprimento: float) -> float:
    """Calcula a área de um retângulo."""
    area = largura * comprimento
    return area

def mostra_cabecalho(simbolo: str, titulo: str) -> None:
    """Mostra um cabeçalho formatado."""
    print(simbolo * len(titulo), f"{simbolo * 4}", sep='')
    print(f'  {titulo}  ')
    print(simbolo * len(titulo), f"{simbolo * 4}", sep='')

mostra_cabecalho('~', 'Cálculo de Área')
area1 = area(5, 10)
mostra_cabecalho('#', 'Resultado')

print(f'A área de um terreno de 5m x 10m é de {area1}m².')
