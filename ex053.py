frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')