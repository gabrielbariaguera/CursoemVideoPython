n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += n 
print('Você digitou {} termos e a soma deles é {}'.format(cont - 1, soma - 999))
