from modulos.interface import *


def arquivo(txt):
    try:
        arq = open(txt, 'rt') #read
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(txt):
    arq = open(txt, 'wt+') #write +
    arq.close()
    print(f'Arquivo {txt} criado com sucesso!')


def lerArquivo(txt):
    try:
        arq = open(txt, 'rt')
    except:
        print(f'Erro ao ler o arquivo {txt}')
    else:
        titulo('USUÁRIOS CADASTRADOS')
        for l in arq:
            inf = l.split(';')
            inf[1] = inf[1].replace('\n', '')
            print(f'{inf[0]:<30}  {inf[1]:>3} anos.')
    finally:
        arq.close()


def cadastrar(txt, nome='desconhecido', id=0):
    try:
        arq = open(txt, 'at') #append
    except:
        print(f'ERRO: o arquivo {txt} não pode ser aberto.')
    else:
        try:
            arq.write(f'{nome};{id}\n')
        except:
            print(f'ERRO: não foi possível escrever no arquivo {txt}.')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        arq.close()