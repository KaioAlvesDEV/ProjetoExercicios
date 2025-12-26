algoritmo "DobroETercaParte"
var

   valor_inicial, dobro, terca_parte : real
   pause : caractere
   
inicio

   mudacor("Amarelo", "Frente")
   
   //Cabeçalho
   escreval("|-D---|")
   escreval("|--e--|")
   escreval("|---T-|")
   escreval("|----P|")
   escreval("|by---|")
   escreval("|-kaio|")
   escreval("")
   
   //Input do valor inicial
   escreval("|-------------------------------------------------|")
   escreval("|ESCREVA UM VALOR PARA VER O DOBRO E A TERÇA PARTE|")
   escreva("|>> ")
   leia(valor_inicial)
   escreval("")
   
   //Pausa
   escreval("------------------------------")
   escreva("aperte ENTER para continuar...")
   leia(pause)
   limpatela
   
   //Processamentp
   dobro <- valor_inicial * 2
   terca_parte <- valor_inicial / 3
   
   //Cabeçalho de novo
   escreval("|-D---|")
   escreval("|--e--|")
   escreval("|---T-|")
   escreval("|----P|")
   escreval("|by---|")
   escreval("|-kaio|")
   escreval("")
   
   //Saída
   escreval("-------------------")
   escreval("DOBRO:", dobro:5:2)
   escreval("TERÇA PARTE:", terca_parte:5:2)
   escreval("-------------------")

   //Pausa de novo
   escreval("------------------------------")
   escreva("aperte ENTER para continuar...")
   leia(pause)
   limpatela
   
   //Cabeçalho... De novo
   escreval("|-D---|")
   escreval("|--e--|")
   escreval("|---T-|")
   escreval("|----P|")
   escreval("|by---|")
   escreval("|-kaio|")
   escreval("")
   
   //Agradecendo o usuário
   escreval("--------------------")
   escreval("OBRIGADO POR USAR :)")
   escreval("--------------------")
   
   //Finalizando o programa
   escreval("--------------------------------------")
   escreval("aperte ESC para encerrar o processo...")
   
fimalgoritmo