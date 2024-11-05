v = int(input('Qual é a velocidade atual do seu carro?'))
if v > 110:
    print('MULTADO! Você excedeu o limite permitido que é de 110Km/h')
    print('Você deve pagar uma multa de R${}'.format(v * 0.80))
print('Tenha um bom dia! Dirija com segurança!')
    