n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
décimo = n + (10 -1) * r
for c in range(n, décimo + r, r):
    print('{}'.format(c), end=' > ')
print('Acabou')   
