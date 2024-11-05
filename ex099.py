def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    for n in num:
        print(f'{n} ', end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1            
    print(f'Foram informados {cont} valores')    
    print(f'O maior valor foi {maior}')


maior(2, 8, 5, 3, 1, 7)
maior(6, 1, 9)
maior(7, 3)    