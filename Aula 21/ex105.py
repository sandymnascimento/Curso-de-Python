def notas (* n, sit=False):
    """
    => Função para analisar notas e a situação de um grupo de alunos.
    :param n: Uma ou mais notas.
    :param sit: valor opcional, indicando se deve ou não informar a situação.
    :return: Um dicionário contendo informações sobre a situação da turma.
    """
    nota = {'Qtd': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': sum(n) / len(n)}

    if sit:
        if nota['Média'] >= 8.5:
            nota['Situação'] = 'Excelente'
        elif nota['Média'] >= 7.5:
            nota['Situação'] = 'Boa'
        elif nota['Média'] >= 5:
            nota['Situação'] = 'Razoável'
        else:
            nota['Situação'] = 'Ruim'
    return nota


notas1 = notas(10, 9, 6, 8, 10, sit=True)
for c, v in notas1.items():
    print(f'{c} = {v}')
print('-' * 20)
notas2 = notas(6, 9, 5)
for c, v in notas2.items():
    print(f'{c} = {v}')
print('-' * 20)
help(notas)