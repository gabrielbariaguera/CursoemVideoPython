resp = 'S'
soma = qnt = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qnt += 1
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num        
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
média = soma / qnt    
print('Você digitou {} números e a média deles é {}'.format(qnt, média))    
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('Acabou')    
