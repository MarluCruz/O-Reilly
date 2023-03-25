def mysqrt(a, x):
    y = None
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

print('Digite um número inteiro para a: ')
a = int(input())

print('Digite um número inteiro para x: ')
x = int(input())

print(mysqrt(a, x))