peso = float(input('Qual seu peso (Kg)? '))
altura = float(input('Qual sua altura (m)? '))
imc = peso / altura ** 2
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está em sobrepeso')
elif imc < 40:
    print('Você está em obesidade')
else:
    print('Você está em obesidade mórbida')
