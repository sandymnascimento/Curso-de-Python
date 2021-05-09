from modulos import dados, preco

p = dados.leiaDinheiro(input('Digite o preço: R$').replace(',', '.').strip())
preco.resumo(p, 20, 12)