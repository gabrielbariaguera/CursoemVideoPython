matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3): #Linhas da matriz
    for c in range(0,3): #Colunas da matriz
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()    