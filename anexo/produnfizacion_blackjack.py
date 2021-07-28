# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

import random
import numpy as np


def crear_jugador(cant_jug=1):
    jugador = {
        'id': 1,
        'nombre': 'Julián',
        'tiros': 0,
        'puntos': 0
    }
    jugadores = []
    for x in range(cant_jug):
        nombre = input(f'Ingrese nombre del jugador nro. {x+1}: ')
        jugador['id'] = x + 1
        jugador['nombre'] = nombre
        jugadores.append(jugador)
    return jugadores


def blackjak_modulo(jugadores):
    pass


if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    print('¡Bienvenidso a Blackjack Python!\nIngrese cantidad de jugadores (Máximo 7):')
    while True:
        cant_jug = int(input())
        if 0 < cant_jug <= 7: break
        else: print('La cantidad de jugadores debe ser entre 1 y 7.')
    
    jugadores = crear_jugador(cant_jug)

    print('¡Que comience el juego!')

    blackjak_modulo(jugadores)

    print("terminamos")