def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1  
    print(f'Contagem de {i} até {f} de {p} em {p}')  
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            cont += p 
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            cont -= p
        print('FIM') 


contador (1, 10, 1)
contador (10, 0, 2)               
print('Agora é sua vez')
ini = int(input('Início: '))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)