#Exercicio1

#Ezimar Júnior - 072320021, Micaele - 072320083, Shelini Dantas - 072320043

print('Hello World')#Amostre a frase Hello World

#print ( Usado para imprimir um comando na tela)

#Para criar uma nova função em Python, a palavra reservada def é utilizada.
Em seguida, é atribuído um nome ao identificador que será usado para chamá-la.
Depois do nome, uma lista opcional de parâmetros é incluída entre parênteses.
O cabeçalho da função termina com dois pontos.
Nas linhas seguintes, com uma indentação maior vem o corpo da função, ou seja, uma sequência de sentenças que executam uma operação.
Por último, opcionalmente, é adicionada a palavra reservada return para devolver um resultado.
Uma vez que a função é definida, você pode reutilizá-la várias vezes no seu programa.

Agora, como exemplo, podemos criar uma função simples de soma com dois parâmetros:
#print ( Usado para imprimir um comando na tela)
#input ( Abre um terminar que permite ser digitado algo que será passado para a função ) 
#.upper( usado para deixa todas as letras digitadas para responder o algoritmo "maiúsculas", os caracteres da string) 
#While( Ela analisa se as instruções do bloco de nota e executa dando uma condição para o mesmo em forma de loop até a condição se atendida ou até a função break)
#break( encerra o loop da função While )
#if( Ela analisa se as instruções do bloco de nota e executa dando uma condição para o mesmo). 
#elif( Serve como condição para executar uma regra. Deve ser usado depois do comando If) ( chama de cláusula If,While,elif,Else )
#else( serve para executar uma ação, caso não esteja condicionada pelos comandos if e elif , sendo sempre usados depois deles, executando caso a comparação if/elif não passe)
#float( utilizado para lidar com números decimais)
#.f ( Usado para específica a quantidade de casas depois da vírgula) 
# == ( igual a) 
# * ( multiplicação)
#!=( diferente )
#len( Informa o número de caracteres ).
#Parâmetro ( O que está entre parênteses) ( Uma variável na definição da função )
#Argumento ( A função definida para o parâmetro) ( é o dado que você passa durante a chamada da função )
# String ( Palavras entre aspas)
# inteiros ( números inteiros, positivos e negativos )
# float ( números racionais, que tem vírgulas )
# variável ( palavra a ser especificado um argumento/ parâmetro)
# módulo ( arquivos do python)
# Script é um texto com uma série de instruções escritas para serem seguidas, ou por pessoas em peças teatrais ou programas televisivos, ou executadas por um programa de computador. 
# Função é um bloco de código que realiza uma tarefa específica.
# Classe ( Classes, em Python, são como moldes que nos permitem criar objetos. Esses objetos, então, podem conter dados (atributos) e funcionalidades (métodos). O uso de classes facilita a organização do código, tornando-o mais modular, reutilizável e fácil de entender).
# Main ( Isso quer dizer que, estamos executando o arquivo de forma direta, ou seja, abrimos o arquivo e estamos executando ele. Dessa forma a variável __name__ recebe o valor __main__. No entanto, quando importamos esse arquivos e executamos através de um segundo arquivo, essa variável recebe outra informação. Então ao fazer a comparação de __name__ = “__main__” ela será falsa e, portanto, não vai executar o conteúdo dessa estrutura.Por esse motivo quando executamos o código diretamente no arquivo ele lê todo o conteúdo da estrutura e quando executamos através da importação do arquivo ele não lê o que está na estrutura. Dessa forma o valor atribuído a variável __name__ é diferente de “__main__”! Isso é interessante quando você vai fazer algum teste no seu arquivo principal, mas não quer que ele seja executado em arquivos secundários, então pode colocar alguma função que só funcione no arquivo principal). 
# Lista ( Uma lista começa com um colchete de abertura e termina com um colchete de fechamento, [ ] . Os valores dentro da lista também são chamados de itens . Os itens são separados por vírgulas (ou seja, são delimitados por vírgulas ). 
# Em vez de usar a técnica range(len( someList )) com um loop for para obter o índice inteiro dos itens na lista, você pode chamar a função enumerate() . Em cada iterajção do loop, enumerate() retornará dois valores: o índice do item na lista e o item na própria lista.
# Uma técnica comum do Python é usar range(len( someList )) com um loop for para iterar sobre os índices de uma lista.cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
size
#Atribuição múltipla (tecnicamente chamado de descompactação de tupla ) é um atalho que permite atribuir múltiplas variáveis com os valores em uma lista em uma linha de código.
# Métodos ( Um método é a mesma coisa que uma função, exceto que é “chamado” por um valor. Por exemplo, se um valor de lista fosse armazenado em spam , você chamaria o método de lista index() nessa lista da seguinte forma: spam.index('hello') . A parte do método vem depois do valor, separada por um ponto). 
# Adicionando valores a listas com os métodos append() e insert(). Para adicionar novos valores a uma lista, use os métodos append() e insert(). ok ok
spam = ['gato', 'cachorro', 'morcego']
spam.append('alce')
spam. spam = ['gato', 'cachorro', 'morcego']
spam.insert(1, 'galinha' )
spam. name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
# Tuplas ( O tipo de dados tupla é quase idêntico ao tipo de dados lista, exceto de duas maneiras. Primeiro, as tuplas são digitadas com parênteses, ( e ) , em vez de colchetes, [ e ] . Mas a principal diferença entre as tuplas e as listas é que as tuplas, assim como as strings, são imutáveis. As tuplas não podem ter seus valores modificados, acrescentados ou removidos). 
#As referências são particularmente importantes para entender como os argumentos são passados para as funções. Quando uma função é chamada, os valores dos argumentos são copiados para as variáveis dos parâmetros. Para listas (e dicionários), isso significa que uma cópia da referência é usada para o parâmetro.
#.copy(),  deepcopy(): Python fornece um módulo chamado copy que fornece as funções copy() e deepcopy() . O primeiro deles, copy.copy() , pode ser usado para fazer uma cópia duplicada de um valor mutável como uma lista ou dicionário, não apenas uma cópia de uma referência.
#Dicionário: Os índices para dicionários são chamados de chaves, e uma chave com seu valor associado é chamada de par chave-valor . No código, um dicionário é digitado entre chaves, {} .
#Quando você usa os métodos keys() , valus() e items() , um loop for pode iterar sobre as chaves, valores ou pares de valores-chave em um dicionário, respectivamente. Observe que os valores no valor dict_items retornado pelo método items() são tuplas da chave e do valor.
# chave é a chave do dicionário que desejamos acessar
# valor_padrao é o valor que será retornado caso a chave não seja encontrada (opcional)
