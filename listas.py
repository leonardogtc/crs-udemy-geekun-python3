"""
Listas

Listas em Python funcionam como arrays/vetores/matrizes em outras linguagens com a diferença de serem 
DINÂMICOS e também de podermos colocar qualquer tipo de dado.

As listas em python são representadas por colchetes []
"""

# Definir uma lista
lista1 = [1, 99, 33, 23, 56, 89, 87, 43]

lista2 = ['G', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(11))

lista5 = ['Geek University']


# A procura dentro de uma lista é muito fácil de fazer
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')
