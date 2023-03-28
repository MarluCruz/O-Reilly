#Podemos escrever instruções de forma mais concisa usando uma espressão condicional

def factorial(n):
    return 1 if n==0 else n * factorial(n-1)    #Exemplo de função recursiva com expressão condicional

class Kangaroo: # Outro uso de expressões condicionais é lidar com argumentos opcionais.
    def __init__ (self, name, contents=None):
        self.name = name
        self.pounch_contents = [] if contents == None else contents
    
    def __str__(self):
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

if __name__ == '__main__':
    print(factorial(4))
"""Em geral, é possível substituir  uma instrução condicional por uma expressão condicional se ambos
 os ramos contiverem expressões simples  que sejam retornadas ou atribuídas à mesma variável"""