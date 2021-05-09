from random import choice

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
nomes = [n1, n2, n3, n4]

print('O aluno(a) sorteado foi: {}!' .format(choice(nomes)))
