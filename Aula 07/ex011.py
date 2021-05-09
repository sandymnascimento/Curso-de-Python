b = int(input('Qual a largura da parede? '))
h = int(input('Qual a altura da parede? '))
area = b * h
print(f'A sua parede possui dimensões de {b} por {h}, portanto possui uma área de {area} m².')
print(f'Para pintar uma parede com {area} m², será necessário {area // 2} litros de tinta.')

