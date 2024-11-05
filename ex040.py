n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é de {}'.format(media))
if media >= 7:
    print('Parabéns, você está aprovado!!')
elif media < 5:
    print('Você está reprovado!')
else:
    print('Você está de recuperação!')
            