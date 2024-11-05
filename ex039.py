from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
if idade == 18:
    print('Você tem que se aliastar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}.'.format((18 - idade) + ano))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18)) 
    print('Seu alistamento foi em {}.'.format((idade - 18) + ano))       
