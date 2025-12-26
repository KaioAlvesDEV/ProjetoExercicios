Algoritmo "Bhaskhara"

Var

   a, b, c, delta, bhaskx1, bhaskx2: real
   pause: caractere

Inicio

   mudacor("Amarelo", "Frente")
   //Cabeçalho
   escreval("|--------------------|")
   escreval("|BHASKHARA CALCULATOR|")
   escreval("|--------(by kaio)---|")
   escreval("|--------------------|")
   escreval("")
   
   //Entrada dos coeficientes
   escreval("----------------------------")
   escreva("INSIRA O VALOR DE 'A' : ")
   leia(a)
   escreva("INSIRA O VALOR DE 'B' : ")
   leia(b)
   escreva("INSIRA O VALOR DE 'C' : ")
   leia(c)
   escreval("----------------------------")
   escreval("")
   escreva("Aperte ENTER para prosseguir...")
   leia(pause)
   
   //Obtendo o valor de delta
   delta <- b^2 - 4 * a * c

   //Limpando e reemprimindo o cabeçalho para melhor organização visual
   limpatela
   
   escreval("|--------------------|")
   escreval("|BHASKHARA CALCULATOR|")
   escreval("|--------(by kaio)---|")
   escreval("|--------------------|")
   escreval("")
   
   //Verificando e imprimindo algo diferenta para todas as excessões de uma...
   //...equação do segundo grau
   se (a = 0) entao
      escreval("|---------------------------------|")
      escreval("|NÃO É UMA EQUAÇÃO DO SEGUNDO GRAU|")
      escreval("|---------------------------------|")
      escreval("")
      escreval("obs: em equações do segundo grau o coeficiente 'a' não pode ser igual a zero")
   senao
      se (delta < 0) entao
         escreval("|-------------------------|")
         escreval("|AS SOLUÇÕES SÃO COMPLEXAS|")
         escreval("|-------------------------|")
         escreval("")
         escreval("obs: a solução não se encontra no conjunto dos números reais, e sim dos complexos")
      senao
         se (delta = 0) entao
            bhaskx1 <- (-b + RaizQ(delta))/(2*a)
            escreval("|---------------------------------------------")
            escreval("|A EQUAÇÃO POSSUI APENAS A RAIZ REAL ", bhaskx1:5:2)
            escreval("|---------------------------------------------")
         senao
            bhaskx1 <- (-b + RaizQ(delta))/(2 * a)
            bhaskx2 <- (-b - RaizQ(delta))/(2 * a)
            escreval("|-------------------------------")
            escreval("|BHASK: (x1: ", bhaskx1:5:2, ", x2: ", bhaskx2:5:2, ")")
            escreval("|-------------------------------")
         fimse
      fimse
   fimse
   
   escreval("")
   escreva("Aperte ENTER para prosseguir...")
   leia(pause)
   
   //Exibindo mensagem agradecendo por usar
   limpatela
   
   escreval("|--------------------|")
   escreval("|BHASKHARA CALCULATOR|")
   escreval("|--------(by kaio)---|")
   escreval("|--------------------|")
   escreval("")
   
   escreval("|--------------------|")
   escreval("|OBRIGADO POR USAR :)|")
   escreval("|--------------------|")
   escreval("")
   escreva("Aperte ESC para encerrar o programa...")
   escreval("")
   
Fimalgoritmo