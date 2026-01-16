#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

const int VALOR_CORRETO_DE_ARGUMENTOS = 2;

//Protótipos
bool temNumeroErradoDeArgumentos(int argc, int valor_correto_de_argumentos);
bool temErros(int argc);
int perguntarAChave(void);
char* perguntarOTexto(void);

int main(int argc, char *argv[])
{
    //Erros
    const bool NUMERO_ERRADO_DE_ARGUMENTOS = temNumeroErradoDeArgumentos(argc, VALOR_CORRETO_DE_ARGUMENTOS);

    const int POSICAO_CHAVE = 1;

    int chave = 0;

    if(temErros(argc))
    {
        if (NUMERO_ERRADO_DE_ARGUMENTOS) 
        {
            chave = perguntarAChave();
        }
    }

    if (!NUMERO_ERRADO_DE_ARGUMENTOS)
    {
        chave = atoi(argv[POSICAO_CHAVE]);
    }

    char texto[1000];
    strcpy(texto, perguntarOTexto());

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

bool temNumeroErradoDeArgumentos(int argc, int valor_correto_de_argumentos)
{
    if(argc != valor_correto_de_argumentos)
    {
        return true;
    }
    return false;
}

bool temErros(int argc)
{
    if(temNumeroErradoDeArgumentos(argc, VALOR_CORRETO_DE_ARGUMENTOS))
    {
        printf("Voce pode usar .\\'CifraDeCesar.exe' chave para maior agilidade\n");
        return true;
    }
    return false;
}

int perguntarAChave(void)
{
    int chave = 0;
    printf("Digite a chave de cifra (numero inteiro): ");
    scanf("%d", &chave);
    getchar();
    return chave;
}

char* perguntarOTexto(void)
{
    static char texto[1000];
    printf("Digite o texto a ser cifrado: ");
    fgets(texto, sizeof(texto), stdin);
    return texto;
}
