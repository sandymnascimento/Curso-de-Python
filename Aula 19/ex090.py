aluno = dict()
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'em Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'{aluno["nome"]} possui média {aluno["media"]} e esta {aluno["situacao"]}.')