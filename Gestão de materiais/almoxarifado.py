from materiais import almoxarifado

print('Itens disponiveis no almoxarifado:')
for item, quantidade in almoxarifado.items():
    print(f'{item}: {quantidade}')

# Utilizar materiais na obra
ceramicas_usadas = int(input('Quantidade de Ceramicas usadas na obra: '))
madeiras_usadas = int(input('Quantidade de Madeira usadas na obra: '))
concretos_usadas = int(input('Quantidade de Concreto usadas na obra: '))
ferros_usadas = int(input('Quantidade de Ferro usadas na obra: '))
calcarios_usados = int(input('Quantidade de Calcario usado na obra: '))
argilas_usadas = int(input('Quantidade de argila usada na obra: '))

# Atualizar quantidade de materiais restantes
almoxarifado['Ceramica'] -= ceramicas_usadas
almoxarifado['Madeira'] -= madeiras_usadas
almoxarifado['Concreto'] -= concretos_usadas
almoxarifado['Ferro'] -= ferros_usadas
almoxarifado['Calcario'] -= calcarios_usados
almoxarifado['Argila'] -= argilas_usadas

# Transformar materiais usados conforme a logica especificada
almoxarifado['Telha'] += ceramicas_usadas // 2
almoxarifado['Tabua'] += madeiras_usadas // 2
almoxarifado['Brita'] += concretos_usadas // 2
almoxarifado['Viga'] += ferros_usadas // 2
almoxarifado['Cimento'] += min(calcarios_usados, argilas_usadas)

print('\nQuantidade restante no almoxarifado apos uso em obras e transformação dos materiais:')
for item, quantidade in almoxarifado.items():
    print(f'{item}: {quantidade}')