num = [[], []]
na = 0
for n in range(1, 8):
    na = int(input(f'Digite o {n}º valor: '))
    if na % 2 == 0:
        num[0].append(na)
    else:
        num[1].append(na)    
print('-=' *30)    
num[0].sort()
num[1].sort()
print(f'Os pares foram {num[0]}')
print(f'O impares foram {num[1]}')
