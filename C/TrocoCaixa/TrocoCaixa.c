/*
    ~ By Kaio Duan Alves Santos ~
                    "Go Slowly"
*/

#include <stdio.h>

const int MOEDAS[6] = {1, 5, 10, 25, 50, 100};
const int INDICE_MAIOR_MOEDA = sizeof(MOEDAS) / sizeof(MOEDAS[0]) - 1;

int pedir_troco_total_em_centavos(void);
int qtd_moedas_devolvidas(int troco_total);
void pausar_programa(void);

int main(void)
{
    int troco_total = pedir_troco_total_em_centavos();
    int qtd_moedas = qtd_moedas_devolvidas(troco_total);

    printf("Moedas devolvidas: %d", qtd_moedas);
    pausar_programa();

    return 0;
}

int pedir_troco_total_em_centavos(void)
{
    int troco_total;
    do{
        printf("Escreva quanto voce ira devolver de troco em centavos: ");
        scanf("%d", &troco_total);
    } while(troco_total < 0);
    getchar();
    return troco_total;
}

int qtd_moedas_devolvidas(int troco_total)
{
    int moeda_atual = INDICE_MAIOR_MOEDA;
    int qtd_moedas = 0;
    while(troco_total != 0)
    {
        while(troco_total - MOEDAS[moeda_atual] < 0)
        {
            moeda_atual -= 1;
        }
        troco_total -= MOEDAS[moeda_atual];
        qtd_moedas += 1;
    }
    return qtd_moedas;
}

void pausar_programa(void)
{
    printf("\nAPERTE ENTER PARA CONTINUAR...");
    getchar();
}
