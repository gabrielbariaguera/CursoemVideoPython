import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
coseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo {} tem o seno de {:.2f}, o coseno de {:.2f} e a tangente de {:.2f}'.format(an, seno, coseno, tangente))
