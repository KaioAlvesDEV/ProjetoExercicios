Algoritmo "ConversorDeComprimento"
Var
   user_input_metros, km, hm, dam, dm, cm, mm : real
   pause : caractere
Inicio

   mudacor("Amarelo", "Frente")

   //LOGO PRINCIPAL
   escreval("|---------------|")
   escreval("|C      C       |")
   escreval("|O      O       |")
   escreval("|N      M       |")
   escreval("|V      P      k|")
   escreval("|E   D  R   b  a|")
   escreval("|R   E  I   y  i|")
   escreval("|S      M      o|")
   escreval("|O      E       |")
   escreval("|R      N       |")
   escreval("|       T       |")
   escreval("|       O       |")
   escreval("|---------------|")
   escreval("")
   
   //MENSAGEM DE BOAS-VINDAS
   escreval("|-----------------------------------------|")
   escreval("|BEM-VINDO AO CONVERSOR DE COMPRIMENTO! :)|")
   escreval("|-----------------------------------------|")
   escreval("")
   
   //PAUSA
   escreval("---------------------------------------")
   escreval("aperte a tecla ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   //MINILOGO E REIMPRESSÃO
   escreval("-*-")
   escreval("CdC")
   escreval("*-*")
   escreval("")

   //INPUT DE METROS
   escreval("|----------------------------------------------------------------------------|")
   escreval("|POR FAVOR, INSIRA O VALOR EM METROS QUE DESEJA CONVERTER PARA OUTRAS MEDIDAS|")
   escreva("|>> ")
   leia(user_input_metros)
   escreval("|----------------------------------------------------------------------------|")
   escreval("")
   
   //PAUSA E REIMPRESSÃO
   limpatela
   escreval("-*-")
   escreval("CdC")
   escreval("*-*")
   escreval("")

   //ADICIONA "m" DEPOIS DO VALOR EM METROS QUE O USUÁRIO BOTOU PARA FICAR BONITO
   escreval("|----------------------------------------------------------------------------|")
   escreval("|POR FAVOR, INSIRA O VALOR EM METROS QUE DESEJA CONVERTER PARA OUTRAS MEDIDAS|")
   escreva("|>> ")
   escreval(user_input_metros, "m")
   escreval("|----------------------------------------------------------------------------|")
   escreval("")
   
   //PAUSA
   escreval("---------------------------------------")
   escreval("aperte a tecla ENTER para prosseguir...")
   leia(pause)
   limpatela

   //PROCESSAMENTO
   km <- user_input_metros / 1000
   hm <- user_input_metros / 100
   dam <- user_input_metros / 10
   dm <- user_input_metros * 10
   cm <- user_input_metros * 100
   mm <- user_input_metros * 1000

   //MINILOGO DE NOVO
   escreval("-*-")
   escreval("CdC")
   escreval("*-*")
   escreval("")
   
   //TABELA DE CONVERSÃO
   escreval("/-----------------------\")
   escreval("|  TABELA DE CONVERSÃO  |")
   escreval("\-----------------------/")
   escreval("|KM:    ", km:4:2, "km")
   escreval("|HM:    ", hm:4:2, "hm")
   escreval("|DAM:   ", dam:4:2, "dam")
   escreval("|DM:    ", dm:4:2, "dm")
   escreval("|CM:    ", cm:4:2, "cm")
   escreval("|MM:    ", mm:4:2, "mm")
   escreval("\-----------------------/")
   escreval("")
   
   //PAUSA
   escreval("---------------------------------------")
   escreval("aperte a tecla ENTER para prosseguir...")
   leia(pause)
   limpatela
   
   //LOGO PRINCIPAL DE NOVO
   escreval("|---------------|")
   escreval("|C      C       |")
   escreval("|O      O       |")
   escreval("|N      M       |")
   escreval("|V      P      k|")
   escreval("|E   D  R   b  a|")
   escreval("|R   E  I   y  i|")
   escreval("|S      M      o|")
   escreval("|O      E       |")
   escreval("|R      N       |")
   escreval("|       T       |")
   escreval("|       O       |")
   escreval("|---------------|")
   escreval("")

   //MENSAGEM DE ENCERRAMENTO
   escreval("|----------------------------------|")
   escreval("|OBRIGADO POR USAR, VOLTE SEMPRE :)|")
   escreval("|----------------------------------|")
   escreval("")
   escreval("--  by kaio  --")
   escreval("")
   
   //ENCERRAMENTO
   escreval("----------------------------------------------")
   escreval("aperte a tecla ESC para encerrar o processo...")
   escreval("")
   
Fimalgoritmo