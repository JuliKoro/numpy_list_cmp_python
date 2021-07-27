# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    # len_string = lambda......
    
    len_string = lambda texto: len(texto)
    texto_ingresado = input('Ingrese un texto: ')
    print(f'Longitud de "{texto_ingresado}": {len_string(texto_ingresado)}\n')

    # 2)
    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto en cada iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    # palabras_len = list(map....)

    palabras_len = list(map(lambda texto: print(f'Longitud de "{texto}": {len(texto)}'), palabras))
    
    print("terminamos")