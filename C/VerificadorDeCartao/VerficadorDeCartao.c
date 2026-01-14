/*
    ~ By Kaio Duan Alves Santos ~
    "Eu te amo, eu te amo, eu já te disse que amo"
*/

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

unsigned long long int numero_cartao;
unsigned long long int ler_numero_cartao(void);
unsigned long long potencia_de_10(int expoente);
int qtd_digitos(unsigned long long int numero);
char* bandeira_cartao(unsigned long long int numero_cartao);
bool validar_numero_cartao_usando_luhn(unsigned long long int numero_cartao);
bool cartao_eh_amex(unsigned long long int numero_cartao);
bool cartao_eh_mastercard(unsigned long long int numero_cartao);
bool cartao_eh_visa(unsigned long long int numero_cartao);
bool cartao_eh_discover(unsigned long long int numero_cartao);
bool cartao_eh_diners_club(unsigned long long int numero_cartao);
bool cartao_eh_nubank(unsigned long long int numero_cartao);

void pausa(void);


int main()
{
    numero_cartao = ler_numero_cartao();
    bool numero_valido = validar_numero_cartao_usando_luhn(numero_cartao);
    printf("O numero do cartao %s valido.\n", numero_valido ? "e" : "nao e");

    if (numero_valido)
    {
        char* bandeira = bandeira_cartao(numero_cartao);
        printf("Bandeira do cartao: %s\n", bandeira);
    }
    else
    {
        printf("INVALIDO\n");
    }

    pausa();

    return 0;
}

unsigned long long int ler_numero_cartao(void)
{
    printf("Digite o numero do cartao: ");
    scanf("%llu", &numero_cartao);
    getchar();

    return numero_cartao;
}

bool validar_numero_cartao_usando_luhn(unsigned long long int numero_cartao)
{
    int soma = 0;
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    bool deve_dobrar;

    if(qtd_digitos_cartao % 2 == 0)
    {
        deve_dobrar = true;
    }
    else
    {
        deve_dobrar = false;
    }

    for (int i = 0; i <= qtd_digitos_cartao - 1; i++)
    {
        unsigned long long divisor = potencia_de_10(qtd_digitos_cartao - 1 - i);
        int digito_atual = (numero_cartao / divisor) % 10;

        if (deve_dobrar)
        {
            digito_atual *= 2;
            if (digito_atual > 9)
            {
                digito_atual -= 9;
            }
        }

        soma += digito_atual;
        deve_dobrar = !deve_dobrar;
    }

    return (soma % 10) == 0;
}

int qtd_digitos(unsigned long long int numero)
{
    int qtd_digitos = 0;
    while(numero != 0)
    {
        numero = numero / 10;
        qtd_digitos++;
    }
    return qtd_digitos;
}

unsigned long long potencia_de_10(int expoente) {
    unsigned long long resultado = 1;
    for (int i = 0; i < expoente; i++) {
        resultado *= 10;
    }
    return resultado;
}

void pausa(void)
{
    printf("\nPressione ENTER para continuar...");
    getchar();
}

char* bandeira_cartao(unsigned long long int numero_cartao)
{
    if(cartao_eh_amex(numero_cartao))
    {
        return "AMEX";
    }
    else if(cartao_eh_mastercard(numero_cartao))
    {
        return "MASTERCARD";
    }
    else if(cartao_eh_visa(numero_cartao))
    {
        return "VISA";
    }
    else if(cartao_eh_discover(numero_cartao))
    {
        return "DISCOVER";
    }
    else if(cartao_eh_diners_club(numero_cartao))
    {
        return "DINERS CLUB";
    }
    else
    {
        return "DESCONHECIDA";
    }
}

bool cartao_eh_amex(unsigned long long int numero_cartao)
{
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    unsigned long long int prefixo_amex = numero_cartao / potencia_de_10(qtd_digitos_cartao - 2);
    return (qtd_digitos_cartao == 15) && (prefixo_amex == 34 || prefixo_amex == 37);
}

bool cartao_eh_mastercard(unsigned long long int numero_cartao)
{
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    unsigned long long int prefixo_mastercard = numero_cartao / potencia_de_10(qtd_digitos_cartao - 2);
    unsigned long long int prefixo_mastercard_novo = numero_cartao / potencia_de_10(qtd_digitos_cartao - 4);
    return (qtd_digitos_cartao == 16) && ((prefixo_mastercard >= 51 && prefixo_mastercard <= 55) || (prefixo_mastercard_novo >= 2221 && prefixo_mastercard_novo <= 2720));
}

bool cartao_eh_visa(unsigned long long int numero_cartao)
{
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    unsigned long long int prefixo_visa = numero_cartao / potencia_de_10(qtd_digitos_cartao - 1);
    return (qtd_digitos_cartao == 13 || qtd_digitos_cartao == 16) && (prefixo_visa == 4);
}

bool cartao_eh_discover(unsigned long long int numero_cartao)
{
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    unsigned long long int prefixo_discover = numero_cartao / potencia_de_10(qtd_digitos_cartao - 4);
    return (qtd_digitos_cartao == 16) && (prefixo_discover == 6011);
}

bool cartao_eh_diners_club(unsigned long long int numero_cartao)
{
    int qtd_digitos_cartao = qtd_digitos(numero_cartao);
    unsigned long long int prefixo_dinners = numero_cartao / potencia_de_10(qtd_digitos_cartao - 3);
    return (qtd_digitos_cartao == 14) && (prefixo_dinners >= 300 && prefixo_dinners <= 305);
}
