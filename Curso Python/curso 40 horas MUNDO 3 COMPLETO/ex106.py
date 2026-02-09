def ajuda(com):
    help(com)

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP')
    comando = str(input('Comando ou Biblioteca > ')).lower().strip()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')



