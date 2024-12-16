import random

def sortear_palavra(lista):
    return random.choice(lista)

def verificarLetra(letra, palavra):
    if letra in palavra:
        return True
    else:
        return False
    
def qtdLetras(palavra):
    i = 0
    arrayLetras = []
    for letra in palavra:
        if letra not in arrayLetras:
            i += 1
            arrayLetras += letra
    return i

    
def exibidor(letras, palavra):
    resultado = ''
    for letra in palavra:
        if letra in letras:
            resultado += letra
        else:
            resultado += '*'
    return resultado