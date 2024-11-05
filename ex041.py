from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Atleta mirim')
elif idade >9 and idade <= 14:
    print('Atleta infantil')
elif idade > 14 and idade <= 19:
    print('Atlets junior')
elif idade > 19 and idade <= 25:
    print('Atleta sênior')
else:
    print('Atleta master') 
                  