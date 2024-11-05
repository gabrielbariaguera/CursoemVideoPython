import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hip = ca*ca + co*co
print('O valor da hipotenusa é {:.2f}'.format(math.sqrt(hip)))
