from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei?'))
num = randint(0, 5)
if n == num:
    print('Parabéns, você conseguiu')
else:
    print('Que pena, voce errou! O número que eu pensei foi {}'.format(num))    
