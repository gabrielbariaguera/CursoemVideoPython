d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
if d > 200:
    print('O preço da sua passagem é de R${}'.format(d * 0.45))
else:
    print('O preço da sua passagem é de R${}'.format(d / 2))
