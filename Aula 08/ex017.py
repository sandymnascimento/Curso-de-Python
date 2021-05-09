from math import hypot

a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
print('Um triângulo com lados medindo {} e {} tem uma hipotenusa que vale é {:.2f}.' .format(a, b, hypot(a,b)))
