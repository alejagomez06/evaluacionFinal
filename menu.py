from caracter import caracter
from palabra1 import palabra
from ascii import ascii
def menu():
    while True:
        print('1. Generar la representación en byte de un carácter\n'
            '2. Generar la representación en byte de una palabra\n'
            '3. Generar la representación ASCII de un byte\n'
            '4. Salir\n')
        opcion = int(input('Digite la opcion que desea: '))
        if opcion == 1:
            letra = input('Digite la letra ')
            print(caracter(letra))
        elif opcion == 2:
            palabra = input('Digite la palabra ')
            print(palabra1(palabra))
        elif opcion == 3:
            codigo = input('Digite el código ')
            print(ascii(codigo))
        elif opcion == 4:
            break
        else:
            print('Digite un número valido')

menu()
    
