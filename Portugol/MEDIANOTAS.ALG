Algoritmo "MediaNotas"

Var
   nota1, nota2, nota3, nota4, media: real
   decoracao: caractere
Inicio

   //Cabeçalho do programa
   escreval("***************")
   escreval("*CALCULA MÉDIA*")
   escreval("*---by kaio---*")
   escreval("***************")
   escreval("")
   
   //Pedindo as notas do usuário
   escreval("**************************")
   escreva("DIGITE A PRIMEIRA NOTA: ")
   leia(nota1)
   escreva("DIGITE A SEGUNDA NOTA: ")
   leia(nota2)
   escreva("DIGITE A TERCEIRA NOTA: ")
   leia(nota3)
   escreva("DIGITE A QUARTA NOTA: ")
   leia(nota4)
   escreval("**************************")
   escreval("")

   //Calculando a média das notas do usuário
   media <- (nota1 + nota2 + nota3 + nota4)/4
   
   //Falando a média da nota do usuário
   escreval("***********************************")
   escreval("A MÉDIA DAS QUATRO NOTAS É DE", media)
   escreval("***********************************")
   escreval("")
   
   //Dizendo se o usuário passou ou não de ano
   se(media >= 6) entao
       decoracao <- "**************"
       escreval(decoracao)
       escreval("PASSOU DE ANO!")
   senao
        decoracao <- "**********"
        escreval(decoracao)
        escreval("REPROVADO!")
   fimse
   escreval(decoracao)
   
Fimalgoritmo