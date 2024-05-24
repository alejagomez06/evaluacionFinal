def ascii(binary_string):
    decimal_value = int(binary_string, 2)
    
    ascii_char = chr(decimal_value)

    hex_value = hex(decimal_value)[2:]  
    
    return f"{ascii_char}-{hex_value}"