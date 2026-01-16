#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//Erros
const int VALOR_CORRETO_DE_ARGUMENTOS = 3;
const int VALOR_NO_INTERVALO_ERRADO = 2;

//Protótipos
int temNumeroErradoDeArgumentos(int argc, int valor_correto_de_argumentos);
int temErros(int argc);

int main(int argc, char const *argv[])
{
    const int POSICAO_CHAVE = 1;
    if(temErros(argc))
    {
        const bool NUMERO_ERRADO_DE_ARGUMENTOS = temNumeroErradoDeArgumentos(argc, VALOR_CORRETO_DE_ARGUMENTOS);

        if (NUMERO_ERRADO_DE_ARGUMENTOS) return 1;
    }

    int chave = atoi(argv[POSICAO_CHAVE]);

    char texto[10000] = "";
    printf("Digite o texto a ser cifrado: ");
    fgets(texto, 10000, stdin);
    printf("Texto original: %s", texto);

    for(int caractere_atual = 0; texto[caractere_atual] != '\n'; caractere_atual++)
    {
        if(texto[caractere_atual] >= 'a' && texto[caractere_atual] <= 'z')
        {
            printf("%c", (texto[caractere_atual] + chave) > 'z' ? texto[caractere_atual] + chave - 26 : texto[caractere_atual] + chave);
        }
        else if(texto[caractere_atual] >= 'A' && texto[caractere_atual] <= 'Z')
        {
            printf("%c", (texto[caractere_atual] + chave) > 'Z' ? texto[caractere_atual] + chave - 26 : texto[caractere_atual] + chave);
        }
        else
        {
            printf("%c", texto[caractere_atual]);
        }
    }

    getchar();

    return 0;
}

int temNumeroErradoDeArgumentos(int argc, int valor_correto_de_argumentos)
{
    if(argc != valor_correto_de_argumentos)
    {
        return true;
    }
    return false;
}

int temErros(int argc)
{
    if(temNumeroErradoDeArgumentos(argc, VALOR_CORRETO_DE_ARGUMENTOS))
    {
        printf("Erro: Numero errado de argumentos.\n");
        printf("Uso correto: ./cifraDeCesar chave texto\n");
        return true;
    }
    return false;
}
