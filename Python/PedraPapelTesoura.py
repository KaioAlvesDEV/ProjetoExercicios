from time import sleep
from random import randint

opcoes_jogo = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0, 2)

print(f'{'PEDRA PAPEL TESOURA':=^75}')
usuario_opcao = input(f'\033[93mVai jogar o quê? ').title()

jogador_perdeu = (usuario_opcao == 'Pedra' and opcoes_jogo[maquina] == opcoes_jogo[1]) or (usuario_opcao == 'Papel' and opcoes_jogo[maquina] == opcoes_jogo[2]) or (usuario_opcao == 'Tesoura' and opcoes_jogo[maquina] == opcoes_jogo[0])

if usuario_opcao not in opcoes_jogo:
    print(f'\033[91mESCOLHA INVÁLIDA')
else:
    #sleep(2.5)
    if str(usuario_opcao) in opcoes_jogo[maquina]:
        print(f'EMPATE! MÁQUINA TAMBÉM JOGOU {opcoes_jogo[maquina].upper()}')
    elif jogador_perdeu:
        print(f'\033[91mPERDEU! MÁQUINA JOGOU {opcoes_jogo[maquina].upper()}')
    else:
        print(f'\033[92mGANHOU! MÁQUINA JOGOU {opcoes_jogo[maquina].upper()}')
input()
