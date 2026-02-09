def escreva(text):
    print( '-' * (len(text) + 2))
    print(f' {text} ')
    print( '-' * (len(text) + 2))

texto = str(input('Digite um texto: '))
escreva(texto)