resultado = 0 
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        resultado += c 
        cont += 1
print('A soma de todos os {} valores múltiplos é {}'.format(cont, resultado))
