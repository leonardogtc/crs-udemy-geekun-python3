
"""
Listas
Listas em Python funcionam como arrays/vetores/matrizes em outras 
linguagens com a diferença de serem 
DINÂMICOS e também de podermos colocar qualquer tipo de dado.
As listas em python são representadas por colchetes []
"""

# Definir uma lista
lista1 = [1, 99, 33, 23, 56, 89, 87, 43, 32, 98, 45, 77, 65, 34, 23, 90, 12]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n',
          'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = ['Geek University']


# A procura dentro de uma lista é muito fácil de fazer
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

# Ordenar uma lista
lista1.sort()
print(lista1)
lista2.sort()
print(lista2)

# Contar o número de ocorrências em uma lista
print(lista1.count(23))
print(lista2.count('e'))

# Adicionar elementos em listas
lista1.append(142)
print(lista1)

'''
Em uma lista somente é possível adicionar um elemento por vez utilizando a 
função "append" Para se adicionar mais elementos individuais deve-se utilizar 
a função extend() passando uma lista dentro da função
'''

lista1.extend([190, 191, 192])
print(lista1)

'''
Se o mesmo procedimento for executado com append(), 
uma lista será inserida dentro de outra
'''
lista1.append([180, 181, 182])
print(lista1)
