#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//Erros
const int VALOR_ERRADO_DE_ARGUMENTOS = 1;
const int VALOR_NO_INTERVALO_ERRADO = 2;

int main(int argc, char const *argv[])
{
    const int ARGUMENTOS_NECESSARIOS = 2;
    const int POSICAO_CHAVE = 1;

    if(argc == 1)
    {
        char chave_str;
        printf("Digite a chave de cifragem (numero inteiro entre 0 e 9): ");
        scanf(" %c", &chave_str);
        getchar();
        argv[POSICAO_CHAVE] = &chave_str;
    }

    if(argc > ARGUMENTOS_NECESSARIOS)
    {
        printf("Muitos argumentos fornecidos.\n");
        return VALOR_ERRADO_DE_ARGUMENTOS;
    }

    if(strlen(argv[POSICAO_CHAVE]) != 1 || argv[POSICAO_CHAVE][0] < '0' || argv[POSICAO_CHAVE][0] > '9')
    {
        printf("Argumento invalido. Deve ser um numero inteiro entre 0 e 9.\n");
        return VALOR_NO_INTERVALO_ERRADO;
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
