#EXERCÍCIO 14

print('Indentificação de sexo')# Mostre indentifiicação de sexo
#Ezimar Júnior - 072320021, Micaele - 072320083, Shelini Dantas - 072320043

sexo=input('Digite F para feminino ou M para masculino:')#A variavel sexo igual a abra a função digite F para feminino ou M para masculino
if sexo == 'F' or sexo == 'f':#Se a variavel sexo é igual a string F ou a variavel sexo igual a string f
    print('Feminino')#Mostre a palavra feminino
elif sexo == 'M' or sexo == 'm':#Se a variavel sexo é igual a string M ou a variavel sexo igual a string m
    print('Masculino')#Mostre a palavra masculino
else:#Outros sem serem condicionados
    print('Sexo Inválido')#Mostre a frase sexo inválido
    
#print (Usado para imprimir/mostrar um comando na tela)
#input (Abre um terminar que permite ser digitado algo que será passado para a função)
#if( Ela analisa se as instruções do bloco de nota e executa dando uma condição para o mesmo)
#or( Serve para inserir comparações entre variaveis, realizando condições de ou)
#elif( Serve como condição para executar uma regra. Deve ser usado depois do comando If)
#else( serve para executar uma ação, caso não esteja condicionada pelos comandos if e elif , sendo sempre usados depois deles, executando caso a comparação if/elif não passe)
