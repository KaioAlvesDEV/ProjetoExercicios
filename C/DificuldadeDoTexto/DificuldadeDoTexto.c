#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    const int TAMANHO_MAXIMO_TEXTO = 100000;

    char texto[TAMANHO_MAXIMO_TEXTO];
    printf("Insira o texto a ser avaliado:\n");
    fgets(texto, sizeof(texto), stdin);

    for(int letra = 0; texto[letra] != '\0'; letra++)
    {
        texto[letra] = toupper((unsigned char) texto[letra]);
    }

    int qtd_letras = 0;
    int qtd_palavras = 0;
    int qtd_sentencas = 0;

    for(int letra = 0; texto[letra] != '\0'; letra++)
    {
        if(texto[letra] == '\n')
        {
            texto[letra] = '\0';
        }

        if(texto[letra] >= 'A' && texto[letra] <= 'Z')
        {
            qtd_letras += 1;
        }

        if(texto[letra] == ' ' || texto[letra] == '\0')
        {
            qtd_palavras += 1;
        }

        if(texto[letra] == '.' || texto[letra] == '!' || texto[letra] == '?')
        {
            qtd_sentencas += 1;
        }
    }

    //Calculo de Coleman-Liau
    float L = (float) qtd_letras / (float) qtd_palavras * 100.0;
    float S = (float) qtd_sentencas / (float) qtd_palavras * 100.0;
    float indice = 0.0588 * L - 0.296 * S - 15.8;
    int grau = round(indice);

    printf("Quantidade de letras: %d\n", qtd_letras);
    printf("Quantidade de palavras: %d\n", qtd_palavras);
    printf("Quantidade de sentencas: %d\n", qtd_sentencas);

    if(grau < 1)
    {
        printf("Grau de dificuldade do texto: Antes do 1o grau\n");
    }
    else if(grau >= 16)
    {
        printf("Grau de dificuldade do texto: 16o grau ou mais\n");
    }
    else
    {
        printf("Grau de dificuldade do texto: %d\n", grau);
    }

    getchar();
    return 0;
}
