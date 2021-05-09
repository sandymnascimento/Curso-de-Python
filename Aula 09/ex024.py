cid = str(input('Qual o nome da sua cidade? '))
cid.strip()
busca = cid.split()
print('A cidade digitada começa com Santo?', 'santo' in busca[0].lower())

# print(cid[:5].upper == 'SANTO')
