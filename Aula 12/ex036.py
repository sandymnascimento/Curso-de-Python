print('-=-' * 7)
print('BANCO DO PROGRAMADOR')
print('-=-' * 7)
print('Para avaliação de crédito para empréstimo é preciso algumas informações.')
casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Em quanto tempo pretende pagar o empréstimo? '))

prestacoes = casa / (anos * 12)
limite = 0.30 * sal

print(
    f'O empréstimo no valor de R${casa:.2f} tem prestações mensais no valor de R%{prestacoes:.2f} para serem pagas ao longo de {anos} ano(s).')
if prestacoes > limite:
    print('O empréstimo foi negado. O valor das prestões excede o seu limite financeiro.')
else:
    print('O empréstimo foi aprovado!')
