from random import randint
lista = []
jogos = []
print('-' *30)
print('    JOGA NA MEGA SENA    ')
print('-' *30)
qnt = int(input('Quantos jogos você quer jogar? '))
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1    
print('-=' *3, f'Sorteando {qnt} jogos ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')