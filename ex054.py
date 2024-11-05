from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if ano - idade >= 18:
        maior += 1
    else: 
        menor += 1
print('Ao todo tivemos {} pessoa maiores de idade \n E também tivemos {} pessoa menores de idade'.format(maior, menor))    
