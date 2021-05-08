from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {num}')
print(f'O maior número foi: {max(num)}')
print(f'O menor número foi {min(num)}')