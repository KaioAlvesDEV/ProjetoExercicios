Algoritmo "RequiredPaint"
Var
   largura_parede_m, altura_parede_m, qts_metros_pinta_1litro, area_parede_mquad: real
   litros_tinta_necessarios : real
   pause : caractere
Inicio

   mudacor("Amarelo", "Frente")

   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("|--------------------************************--------------------|")
   escreval("|จจจจจจจจจจจจจจจจจจจจBOAS-VINDAS AO REQPAINT!จจจจจจจจจจจจจจจจจจจจ|")
   escreval("|descubra quantos litros de tinta vai usar para pintar uma parede|")
   escreval("|--------------------************************--------------------|")
   escreval("")
   escreval("")
   
   escreval("               จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                 aperte ENTER para prosseguir...")
   leia(pause)
   limpatela

   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")
   
   escreval("             |------------------------------------|")
   escreval("             |INSIRA A LARGURA DA PAREDE EM METROS|")
   escreva("             |>>  ")
   leia(largura_parede_m)
   limpatela
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("             |------------------------------------|")
   escreval("             |INSIRA A LARGURA DA PAREDE EM METROS|")
   escreval("             |>> ", largura_parede_m, "m")
   escreval("             |------------------------------------|")
   escreval("")
   escreval("")
   
   escreval("               จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                 aperte ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("             |-----------------------------------|")
   escreval("             |INSIRA A ALTURA DA PAREDE EM METROS|")
   escreva("             |>>  ")
   leia(altura_parede_m)
   limpatela
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("             |-----------------------------------|")
   escreval("             |INSIRA A ALTURA DA PAREDE EM METROS|")
   escreval("             |>> ", altura_parede_m, "m")
   escreval("             |-----------------------------------|")
   escreval("")
   escreval("")

   escreval("              จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                aperte ENTER para prosseguir...")
   leia(pause)
   limpatela

   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")
   
   escreval("    |--------------------------------------------------------|")
   escreval("    |INSIRA QUANTOS METROS QUADRADOS PINTAM UM LITRO DE TINTA|")
   escreva("    |>>  ")
   leia(qts_metros_pinta_1litro)
   limpatela
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("    |--------------------------------------------------------|")
   escreval("    |INSIRA QUANTOS METROS QUADRADOS PINTAM UM LITRO DE TINTA|")
   escreval("    |>> ", qts_metros_pinta_1litro, "m2 por litro de tinta")
   escreval("    |--------------------------------------------------------|")
   escreval("")
   escreval("")

   escreval("              จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                aperte ENTER para prosseguir...")
   leia(pause)
   limpatela

   area_parede_mquad <- largura_parede_m * altura_parede_m
   litros_tinta_necessarios <- area_parede_mquad / qts_metros_pinta_1litro
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")
   
   escreval("|----------------------------------------------------------------|")
   escreval("|มREA TOTAL DA PAREDE  : ", area_parede_mquad:4:1, "m2")
   escreval("|LITROS DE TINTA NECESSมRIOS PARA PINTAR A PAREDE  : ", litros_tinta_necessarios:4:1)
   escreval("|----------------------------------------------------------------|")
   escreval("")
   escreval("")
   
   escreval("              จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                aperte ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   escreval("                          |----------|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จreqPAINTจ|")
   escreval("                          |จจจจจจจจจจ|")
   escreval("                          |จbyจจkaioจ|")
   escreval("                          |----------|")
   escreval("")

   escreval("  |--------------------********************--------------------|")
   escreval("  |จจจจจจจจจจจจจจจจจจจจOBRIGADO POR USAR :)จจจจจจจจจจจจจจจจจจจจ|")
   escreval("  |--------------------********************--------------------|")
   escreval("")
   escreval("")

   escreval("                จจจจจจจจจจจจจจจจจจจจจจจจจจจจจจจ")
   escreval("                  aperte ESC para encerrar...")

Fimalgoritmo