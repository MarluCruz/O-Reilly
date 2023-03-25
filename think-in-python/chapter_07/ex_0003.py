import math
def eval_loop():
    while True:
        print('Escreva algo para avaliação eval:')
        text = str(input())
        if text == 'done':
            return resultado
        resultado = eval(text) 
        print(resultado)

print(eval_loop())