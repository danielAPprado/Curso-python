def voto(data):
    from datetime import date
    atual = date.today().year
    idade = atual - data
    if idade <18:
        return(print(f'Para idade {idade} voto RECUSADO')) 
    if 18 <= idade <= 60:
        return(print(f'Para idade {idade} voto OBRIGATORIO')) 
    if idade > 60:
        return(print(f'Para idade {idade} voto OPICIONAL'))

d = int(input('Qual sua data de nascimento? '))
voto(d)  #data = int(input('Qual sua data de nascimento? ')))   duas formas de fazer
