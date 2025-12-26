algoritmo "RealToDolar"
var
   valor_real, valor_dolar, cotacao_dolar_para_real: real
   pause: caractere
inicio

   mudacor("Amarelo", "Frente")

   //BOAS-VINDAS
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 1 de 5")
   escreval("")

   escreval("*---------------------------------------------*")
   escreval("*BEM-VINDO AO CONVERSOR DE REAL PARA DÓLAR! :)*")
   escreval("*---------------------------------------------*")
   escreval("")
   escreval("")
   
   escreval("*-----------------------------*")
   escreval("aperte ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   //PASSO 1
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 2 de 5")
   escreval("")
   
   escreval("*--------------------------------------------------*")
   escreval("*INSIRA A COTAÇÃO DE 1 DÓLAR PARA REAIS HOJE ABAIXO*")
   escreva("*>> ")
   leia(cotacao_dolar_para_real)
   limpatela
   
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 2 de 5")
   escreval("")

   escreval("*--------------------------------------------------*")
   escreval("*INSIRA A COTAÇÃO DE 1 DÓLAR PARA REAIS HOJE ABAIXO*")
   escreval("*>> R$", cotacao_dolar_para_real)
   escreval("*--------------------------------------------------*")
   escreval("")
   escreval("")
   
   escreval("*-----------------------------*")
   escreval("aperte ENTER para prosseguir...")
   leia(pause)
   limpatela

   //PASSO 2
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 3 de 5")
   escreval("")
   
   escreval("*----------------------------------------------------------------*")
   escreval("*INSIRA O VALOR EM REAIS QUE DESEJA CONVERTER PARA DÓLARES ABAIXO*")
   escreva("*>> ")
   leia(valor_real)
   limpatela
   
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 3 de 5")
   escreval("")
   
   escreval("*----------------------------------------------------------------*")
   escreval("*INSIRA O VALOR EM REAIS QUE DESEJA CONVERTER PARA DÓLARES ABAIXO*")
   escreval("*>> R$", valor_real)
   escreval("*----------------------------------------------------------------*")
   escreval("")
   escreval("")

   escreval("*-----------------------------*")
   escreval("aperte ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   
   //PROCESSAMENTO
   valor_dolar <- valor_real / cotacao_dolar_para_real
   
   //SAÍDA
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 4 de 5")
   escreval("")
   
   escreval("*----------------------------------------------------------------------------*")
   escreval("*", valor_real:5:2, " REAIS EM DÓLAR RESULTA EM ", valor_dolar:5:2, " DÓLARES!")
   escreval("*----------------------------------------------------------------------------*")
   escreval("")
   escreval("")
   
   escreval("*-----------------------------*")
   escreval("aperte ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   //FINALIZAÇÃO
   escreval(" $$$$$$$$$$$$$")
   escreval("$.............$")
   escreval("$-> RsToDol <-$")
   escreval("$..by...kaio..$")
   escreval(" $$$$$$$$$$$$$")
   escreval("")
   escreval("tela 5 de 5")
   escreval("")
   
   escreval("*------------------------------------*")
   escreval("*OBRIGADO POR USAR NOSSO PROGRAMA! :)*")
   escreval("*------------------------------------*")
   escreval("")
   escreval("-   presented  by  kaio   -")
   escreval("")
   escreval("")
   
   escreval("*--------------------------------------*")
   escreval("*aperte ESC para encerrar o processo...*")
   leia(pause)
   
fimalgoritmo