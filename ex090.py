alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = int(input('Média do aluno: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'        
print('-=' *30)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
