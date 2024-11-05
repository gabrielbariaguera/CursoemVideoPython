lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)        
print('-=' *30)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {par}')
print(f'A lista de números imapres é {impar}')
