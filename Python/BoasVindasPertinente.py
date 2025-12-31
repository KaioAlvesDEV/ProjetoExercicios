from pathlib import Path

arquivo = Path("nome_usuario")

if arquivo.exists():
    with open("nome_usuario", "r") as arquivo:
        nome = arquivo.read()
else:
    with open("nome_usuario", "w") as arquivo:
        nome = input('Qual o seu nome? ').strip().title()
        arquivo.write(nome)
        
print(f"Seja bem vindo {nome}!")
