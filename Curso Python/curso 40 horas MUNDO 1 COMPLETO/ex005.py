aa = str(input('Digite uma frase ')).upper().strip()
print('Na sua frase existem {} letras A'.format(aa.count('A')))
print('Na sua frase a posição da primeira letra A é {}'.format(aa.find('A')+1))
print('Na sua frase a posição da ultima letra A é {}'.format(aa.rfind('A')+1))