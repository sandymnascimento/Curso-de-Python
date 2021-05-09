from modulos.interface import *
from modulos.arquivo import *
from time import sleep

arq = 'listaDeCadastrados.txt'
if not arquivo(arq):
    criarArquivo(arq)

while True:
    res = menu(['Cadastrar novo usuário.', 'Exibir cadastrados.', 'Sair do sistema.'])
    if res == 1:
        titulo('NOVO CADASTRO')
        nome = input('Nome:  ')
        id = leiaInt('Idade: ')
        cadastrar(arq, nome, id)
    elif res == 2:
        lerArquivo(arq)
    elif res == 3:
        titulo('Saindo do sistema... até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)