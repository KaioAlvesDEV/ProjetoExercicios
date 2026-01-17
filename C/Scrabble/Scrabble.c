#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

//Protótipos
void mostrarJogadorVencedor(int pontuacao_jogadores[2]);
void mostrarPontuacaoJogadores(int pontuacao_jogadores[2]);
void calcularPontuacao(char palavra[], const int valor_letra[], int *pontuacao);
void pedirPalavras(char respostas_jogadores[2][50]);
void uppercs(char str[]);

int main(void)
{
    char respostas_jogadores[2][50];
    const int valor_letra[] = {
        1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
        5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
        1, 4, 4, 8, 4, 10
    };

    pedirPalavras(respostas_jogadores);

    int pontuacao_jogadores[2] = {0, 0};

    for(int jogador = 0; jogador < 2; jogador++)
    {
        calcularPontuacao(respostas_jogadores[jogador], valor_letra, &pontuacao_jogadores[jogador]);
    }
    
    mostrarPontuacaoJogadores(pontuacao_jogadores);
    mostrarJogadorVencedor(pontuacao_jogadores);

    getchar();

    return 0;
}

void mostrarJogadorVencedor(int pontuacao_jogadores[2])
{
    if(pontuacao_jogadores[0] > pontuacao_jogadores[1])
    {
        printf("Jogador 1 vence!\n");
    }
    else if(pontuacao_jogadores[1] > pontuacao_jogadores[0])
    {
        printf("Jogador 2 vence!\n");
    }
    else
    {
        printf("Empate!\n");
    }
}

void mostrarPontuacaoJogadores(int pontuacao_jogadores[2])
{
    printf("Pontuacao Jogador 1: %d\n", pontuacao_jogadores[0]);
    printf("Pontuacao Jogador 2: %d\n", pontuacao_jogadores[1]);
}

void calcularPontuacao(char palavra[], const int valor_letra[], int *pontuacao)
{
    for (int i = 0; palavra[i] != '\0'; i++)
    {
        if (isalpha((unsigned char)palavra[i]))
        {
            int indice = palavra[i] - 'A';
            *pontuacao += valor_letra[indice];
        }
    }
}

void pedirPalavras(char respostas_jogadores[2][50])
{
    for(int jogador = 0; jogador < 2; jogador++)
    {
        printf("Jogador %d, insira sua palavra: ", jogador + 1);
        fgets(respostas_jogadores[jogador], 50, stdin);
        uppercs(respostas_jogadores[jogador]);
    }
}

void uppercs(char str[]) 
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        str[i] = toupper((unsigned char)str[i]);
    }
}
