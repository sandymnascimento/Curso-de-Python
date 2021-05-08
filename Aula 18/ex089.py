turma = list()
print('- ' * 10)
print('  Boletim Escolar')
print('- ' * 10)
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    turma.append([nome, [n1, n2], media])
    res = input('Deseja continuar? ').strip()[0]
    if res in 'Nn':
        break
print('=' * 20)
print(f'{"No.":<4}{"Nome":<10}{"Média":>4}')
print('-' * 20)
for c, a in enumerate(turma):
    print(f'{c:<4}{a[0]:<10}{a[2]:>4.1f}')
print('=' * 20)
while True:
    print('-' * 95)
    aluno = int(input('Para consultar as notas de um aluno, digite o número correspondente: [999 para encerrar] '))
    if aluno == 999:
        print('Finalizando...')
        break
    if aluno < len(turma) and aluno >= 0:
        print(f'As notas de {turma[aluno][0]} foram {turma[aluno][1]}.')
print('Programa encerrado! Volte sempre.')