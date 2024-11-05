fr = input('Digite uma frase:').strip()
print('A letra A aparece {} vezes na frase.'.format(fr.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(fr.upper().find('A')))
print('A úlrima letra A apareceu na posição {}'.format(fr.upper().rfind('A')))
