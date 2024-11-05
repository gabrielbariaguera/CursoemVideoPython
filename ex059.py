print('Digite dois valores:')
n1 = int(input('Primeiro valor '))
n2 = int(input('Segundo valor '))
sair = False
op = 0
while op !=5 :
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        print('=' * 20)
    elif op == 2:
        print('{} X {} é {}'.format(n1, n2, n1 * n2))
        print('=' * 20)
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
            print('=' * 20)
        else:
            print('{} é maior que {}'.format(n2, n1))
            print('=' * 20)
    elif op == 4:
        n1 = int(input('Primeiro valor '))
        n2 = int(input('Segundo valor '))
        print('=' * 20)
    elif op == 5:
        print('Saindo do programa...')    
    else:
        print('Opção inválida.')        
