def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite apenas um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar este número')
            return 0
        else:
            return n