n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 aparecei {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 foi digitado pela primeira vez na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')    
print('Os valores pares digitados foram ', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
