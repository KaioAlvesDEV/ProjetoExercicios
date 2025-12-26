Algoritmo "AntecessorESucessor"

Var

   num, antecessor, sucessor: inteiro

Inicio

   //Cabeçalho
   escreval("|---------------------|")
   escreval("|ANTECESSOR E SUCESSOR|")
   escreval("|-------by kaio-------|")
   escreval("|---------------------|")
   escreval("")
   
   //Inputs
   escreval("------------------------------------------------------")
   escreva("DIGITE UM NÚMERO PARA VER O ANTECESSOR E SUCESSOR: ")
   leia(num)
   escreval("------------------------------------------------------")
   escreval("")
   
   //Processamento de dados
   antecessor <- num - 1
   sucessor <- num + 1
   
   //Saída
   escreval("--------------")
   escreval("ANTECESSOR:", antecessor)
   escreval("SUCESSOR:", sucessor)
   escreval("--------------")
   
Fimalgoritmo