casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual seu salário? R$'))
ano = int(input('Em quantos anos você quer pagar?'))
prestação = casa / (ano * 12)
print('Para pagar uma casa de R${} em {}anos a prestação será de R${:.2f} por mês'.format(casa, ano, prestação))
if prestação > (30 / 100) * sal:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')    