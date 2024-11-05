dado = []
pessoas = []
maipeso = menpeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maipeso = menpeso = dado[1]
    else:
        if dado[1] > maipeso:
            maipeso = dado[1]
        if dado[1] < menpeso:
            menpeso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
    
print('-=' *30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maipeso}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maipeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menpeso}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menpeso:
        print(f'[{p[0]}]', end=' ')
print()
