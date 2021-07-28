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


si = ['1', 'Si', 'si', 'S', 's', 'SI', 'sI']
no = ['2', 'No', 'no', 'N', 'n', 'NO', 'nO']


def crear_jugador(cant_jug=1):
    jugador = {
        'id': 1,
        'nombre': 'Nombre',
        'tiros': 0,
        'puntos': 0,
        'turno': True
    }
    jugadores = []
    for x in range(cant_jug):
        nombre = input(f'Ingrese nombre del jugador nro. {x+1}: ')
        jugador['id'] = x + 1
        jugador['nombre'] = nombre
        jugadores.append(jugador)
    return jugadores


def blackjak_modulo(jugadores):
    salida = 0
    while True:
        for x in range(len(jugadores)):
            if jugadores[x]['turno'] == True:
                tirada = [random.randrange(1,10) for x in range(2)]
                tirada_vec = np.asanyarray(tirada)
                jugadores[x]['puntos'] += np.sum(tirada_vec)
                jugadores[x]['tiros'] += 1
                if jugadores[x]['puntos'] > 21: 
                    jugadores[x]['puntos'] -= np.sum(tirada_vec)
                    jugadores[x]['tiros'] -= 1
                    salida += 1
                elif jugadores[x]['puntos'] == 21: break
                print(f"Tirada nro. {jugadores[x]['tiros']} de {jugadores[x]['nombre']}: {tirada}",
                    f"Puntos: {jugadores[x]['puntos']}\n")
                jugadores[x]['turno'] = False
            else:
                proximo = input('¿Quiere volver a tirar?\n1. Si\n2. No\n')
                if proximo in si: jugadores[x]['turno'] = True
                elif proximo in no: 
                    salida += 1
                    break
                else: print('Por favor ingrese correctamente una de las opciones.')
        if salida == len(jugadores): break
            

def tabla_de_puntos(jugadores):
    tabla = sorted(jugadores, key=lambda i: i['puntos'], reverse=True)
    print("Tabla de puntos:\n", tabla)
    print(f"¡El ganador es {tabla[0]['nombre']} con {tabla[0]['puntos']} puntos en {tabla[0]['tiros']} tiradas!")


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
    ronda = 'si'
    while ronda in si:
        print('¡Que comience el juego!')
        blackjak_modulo(jugadores)
        print('\n¡Fin de la partida!')
        tabla_de_puntos(jugadores)
        while True:
            ronda = input('¿Quiere/n volver a jugar?\n1. Si\n2. No\n')
            if ronda in si or ronda in no: break
            else: print('Por favor ingrese correctamente una de las opciones.')
    print("terminamos")