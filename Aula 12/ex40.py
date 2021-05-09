n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'REPROVADO! A sua média final é de {media:.1f}, portanto você não obteve a nota mínima para ser aprovado na matéria.')
elif 5.0 <= media < 7:
    print(f'RECUPERAÇÃO! A sua média final foi de {media:.1f} e você está em recuperação.')
else:
    print(f'APROVADO! Parabéns, você teve um aproveitamento de {media:.1f}.')
