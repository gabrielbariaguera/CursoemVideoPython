lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont +=1
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r in 'Nn':
        break
print(f'Você digitou {cont} elementos')    
lista.sort()
print(f'Os valores em ordem decrescente são {lista[::-1]}')    
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')    