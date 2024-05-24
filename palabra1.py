def palabra(letras):
    resultado = ''
    for letra in letras:
        binario = ord(letra)
        resultado += {' ' + binario}
    return resultado