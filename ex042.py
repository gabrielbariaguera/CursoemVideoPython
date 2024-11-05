s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
    print('Não é possível formar um triângulo')
else:
    if s1 == s2 and s1 == s3:
        print('O triângulo será equilátero')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('O triângulo será isóceles')
    else: 
        print('O triângulo será escaleno')
                   