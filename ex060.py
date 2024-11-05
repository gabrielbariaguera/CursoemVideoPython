from math import factorial
n = int(input('Digite um número para calcular seu fatorial:'))
f = factorial(n)
c = n
print('Calculando {}! = '.format(n), end = ' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end = ' ')
    c-= 1
    # f *= c funcionaria tbm para fazer o fatorial, mas com o módulo é mais suave
print('{}'.format(f))
