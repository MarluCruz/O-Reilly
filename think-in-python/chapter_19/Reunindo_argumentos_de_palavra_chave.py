"""Se tiver um dicionário de palavras-chave e valores, pode usar o operador de dispersão, **, para chamar uma função:"""
from collections import namedtuple
d = dict(x=1, y=2)
Point = namedtuple('Point', ['x', 'y'])
print(Point(**d))
"""Sem o operador de dispersão, a função trataria d como um único argumento posicional, e então atribuiria d a x e se queixaria porque não há nada para atribuir a y. Quando estiver trabalhando com funções com um grande número de parâmetros, muitas vezes é útil criar e usar dicionários que especifiquem as opções usadas frequentemente"""