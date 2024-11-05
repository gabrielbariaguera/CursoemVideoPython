def área(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar}x{com} é de {a}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))    
área(l, c)