#include <stdio.h>
#include <stdbool.h>
#include <locale.h>

const int INDICE_INICIAL = 0;

void desenhar_escada(int tamanho_escada);

int main(void)
{
    setlocale(LC_ALL, "pt_BR.UTF-8");

    const int AJUSTE_INDICE = 1;
    const int MENOR_VALOR_VALIDO_ESCADA = 1;
    int tamanho_escada;

    printf("Digite o tamanho da escada: ");
    scanf("%d", &tamanho_escada);

    while(tamanho_escada < MENOR_VALOR_VALIDO_ESCADA)
    {
        printf("Valor inválido! Digite o tamanho da escada: ");
        scanf("%d", &tamanho_escada);
    }
    getchar();
    tamanho_escada -= AJUSTE_INDICE;
    
    desenhar_escada(tamanho_escada);

    getchar();

    return 0;
}

void desenhar_escada(int tamanho_escada)
{
    for(int linha = INDICE_INICIAL; linha <= tamanho_escada; linha++)
    {
        for(int coluna = INDICE_INICIAL; coluna <= tamanho_escada; coluna++)
        {
            bool mostrar_asterisco = coluna + linha >= tamanho_escada;
            if(mostrar_asterisco)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }

        for(int preenchimento = linha; preenchimento > 0; preenchimento--)
        {
            printf("*");
        }

        printf("\n");
    }
}   
