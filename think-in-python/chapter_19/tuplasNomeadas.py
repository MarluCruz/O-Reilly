"""O primeiro argumento é o nome da classe que você quer criar. O segundo é uma lista dos atributos que o objeto Point deve ter, como strings o valor de retorno de namedtuple é um objeto de classe."""
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p) # O método init atribui os argumentos a atributos usando os nomes que você forneceu. O método str exibe uma representação do objeto point e seus atributos.

print(p.x)
print(p.y)

print(p[0], p[1])
"""Tuplas nomeadas fornecem uma forma rápida de definir classes simples. O problema é que classes não ficam sempre simples. Mais adiante você poderá decidir que quer acrescentar métodos a uma tupla nomeada. Nesse caso, você poderá definir uma nova classe que herde uma tupla nomeada:"""

class Pointier(Point):
    print()
