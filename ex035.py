r1 = float(input('Digite o primeiro segmento de reta:'))
r2 = float(input('Digite o segundo segmento de reta:'))
r3 = float(input('Digite o terceiro segmento de reta:'))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não é possível formar um triangulo')
else:
    print('É possível formar um triangulo')  
  