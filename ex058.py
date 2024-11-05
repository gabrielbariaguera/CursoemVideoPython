from random import randint
l = randint(0, 10)
print('Acabei de pensat em um número entre 0 e 10.')
print('Será que você consegue advivinhar qual foi?')
n = int(input('Qual é seu palpite? '))
t = 0
acertou = False
while not acertou:
    if n < l:
        print('Mais... Tente mais uma vez.')
        n = int(input('Qual é seu palpite? '))
        t += 1
    elif n > l:
        print('Menos... Tente mais uma vez.')
        n = int(input('Qual é seu palpite? '))
        t += 1
    else:
        acertou = True
        t += 1
print('Acertou com {} tentativas. Parabéns!'.format(t))
