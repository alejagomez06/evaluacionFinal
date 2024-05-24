def ascii(binary_string):
    valorDecimal = int(binary_string, 2)
    
    caracterAscii = chr(valorDecimal)

    valorHexagecimal = hex(valorDecimal)[2:]  
    
    return f"{caracterAscii}-{valorHexagecimal}"