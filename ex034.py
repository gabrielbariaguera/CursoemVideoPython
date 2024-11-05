sal = float(input('Qual é o salário do funcionário? R$'))
if sal >= 5000:
    print('Quem ganhava R${} passa a ganhar R${} agora.'.format(sal, sal + (10 / 100 * sal)))
else:
    print('Quem ganhava R${} passa a ganhar R${} agora.'.format(sal, sal + (15 / 100 * sal)))    
