def palabra(palabra):
    resultado = ''
    for letra in palabra:
        binario = ord(letra)
        resultado += {' ' + binario}
    return resultado