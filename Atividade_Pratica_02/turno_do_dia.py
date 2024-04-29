#EXERCÍCIO23

#Ezimar Júnior - 072320021, Micaele - 072320083, Shelini Dantas - 072320043

turno = input('Digite seu turno, M - matutino, V - vespetino, N - noturno:').upper() #variavel turno igual a abra o terminal: Digite seu turno, M - matutino, V - vespetino,N - noturno. Deixe todas as letras maiusculas
if turno == 'M': #Se a variavel turno for igual a string M
    print('Bom Dia!') #Mostre a frase Bom Dia!
elif turno == 'V': #E se turno for igual a string V
    print('Boa Tarde!') #Mostre a frase Boa Tarde!
elif turno == 'N': #E se turno for igual a string N
    print('Boa Noite!') #Mostre a frase Boa Noite!
else: #Outros que nao foram condicionados
    print('Valor inválido!') #Mostre a frase Valor inválido!

#input( Abre um terminar que permite ser digitado algo que será passado para a função)
#.upper( Usado para deixa todas as letras digitadas para responder o algoritmo "maiúsculas", os caracteres da string) 
#print( Usado para imprimir um comando na tela)
#if( Ela analisa se as instruções do bloco de nota e executa dando uma condição para o mesmo). 
#elif( Serve como condição para executar uma regra. Deve ser usado depois do comando If)
#else( Serve para executar uma ação, caso não esteja condicionada pelos comandos if e elif , sendo sempre usados depois deles, executando caso a comparação if/elif não passe)
#=(Igual)
#==(Igual a)
