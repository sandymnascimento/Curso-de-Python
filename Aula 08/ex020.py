from random import sample, shuffle

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
nomes = [n1, n2, n3, n4]

shuffle(nomes) #Posso apresentar a lista logo após o embaralhamento
print('Os nomes foram sorteados e a ordem de apresentação será:', sample(nomes, 4))
