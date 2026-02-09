from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'
if not arqExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadrastradas', 'Cadrastrar pesoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\nSAINDO DO SISTEMA')
        break
    else:
        print('\nERRO! Digite uma opção válida')
    sleep(2)