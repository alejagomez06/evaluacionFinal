def palabra(letras):
    resultado = ''
    for letra in letras:
        binario = ord(letra)
        final = bin(binario)
        resultado += ' '
        resultado += str(final)
    return resultado