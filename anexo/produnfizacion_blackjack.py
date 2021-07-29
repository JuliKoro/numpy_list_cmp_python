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

# Listas globales usadas para chequear respuestsa en varias funciones
si = ['1', 'Si', 'si', 'S', 's', 'SI', 'sI']
no = ['2', 'No', 'no', 'N', 'n', 'NO', 'nO']


def crear_jugador(cant_jug=1):
    '''Crear Jugadores

    Se ingresan los datos y se crean los perfiles de los jugadores
    Retorna una lista de diccionarios de los jugadores
    @param cant_jug Cantidad de jugadores (default 1)
    '''
    jugador = { # Diccionario con datos del jugador
        'id': 1,
        'nombre': 'Nombre',
        'tiros': 0,
        'puntos': 0,
        'turno': True # Verifica si vuelve a tirar
    }
    jugadores = []
    for x in range(cant_jug): # Se registran los jugadores y se crea la lista
        nombre = input(f'Ingrese nombre del jugador nro. {x+1}: ')
        jugador['id'] = x + 1
        jugador['nombre'] = nombre
        jugadores.append(jugador)
    return jugadores


def blackjak_modulo(jugadores):
    '''Módulo de Blackjack

    Procesa el juego, cuenta los puntos e interactua con el jugador.
    @param jugadores Lista de diccionarios de los jugadores
    '''
    salida = 0 # Variable para contar los jugadores que se bajan de la repartida
    while True:
        for x in range(len(jugadores)):
            if jugadores[x]['turno'] == True: # Cuando el jugador empieza o quiere volver a tirar
                tirada = [random.randrange(1,10) for x in range(2)] # Genero la lista de dos nros. aleatorios
                tirada_vec = np.asanyarray(tirada) # Convierto la lista en un vector de np para agilizar el procesamiento
                jugadores[x]['puntos'] += np.sum(tirada_vec) # Suumo y acumulo los puntos
                jugadores[x]['tiros'] += 1 # Cuento las tiradas
                if jugadores[x]['puntos'] > 21: # Cuenado supera los 21 puntos
                    jugadores[x]['puntos'] -= np.sum(tirada_vec) # Resto los últimos puntos
                    jugadores[x]['tiros'] -= 1 # Resto la tirada
                    salida += 1 # Sumo a un jugador que ya no tira más
                elif jugadores[x]['puntos'] == 21: # Si llega justo a los 21 termina
                    salida += 1
                    break 
                print(f"Tirada nro. {jugadores[x]['tiros']} de {jugadores[x]['nombre']}: {tirada}",
                    f"Puntos: {jugadores[x]['puntos']}\n") # Imprimo info de la tirada
                jugadores[x]['turno'] = False # El jugador no tira hasta que le pregunte
            else:
                proximo = input('¿Quiere volver a tirar?\n1. Si\n2. No\n')
                if proximo in si: jugadores[x]['turno'] = True # El jugador vuelve a tirar
                elif proximo in no: 
                    salida += 1
                    break
                else: print('Por favor ingrese correctamente una de las opciones.')
        if salida == len(jugadores): break # Cuando todos los jugadores no tiran más
            

def tabla_de_puntos(jugadores):
    '''Imprimir Tabla de Puntos

    Imprime una tabla de puntos ordenada con los datos de los jugadores
    y anuncia el ganador o si hay empate.
    @param jugadores Lista de diccionarios de los jugadores
    '''
    empatados = 0 # Variable que cuenta la cantidad de jugadores empatados
    tabla = sorted(jugadores, key=lambda i: i['puntos'], reverse=True) # Ordeno la lista de jugadores según el puntaje de forma descendente
    cabeza = [x.upper() for x in list(tabla[0].keys())] # Mayúscula para las keys que van impresas en pantalla
    print("Tabla de puntos:\n", 'POS. ', cabeza[1], ' ', cabeza[2], ' ', cabeza[3], '\n') # Cabeza de la tabla
    for i in range(len(jugadores)): # Imprimo la info en la tabla
        contenido = list(tabla[i].values())
        print(f"  {i+1}\t{contenido[1]}\t{contenido[2]}\t{contenido[3]}\n")
        if tabla[0]['puntos'] == tabla[i]['puntos']: empatados += 1 # Cuento los empatados en primer puesto en caso de que haya
    if empatados > 0: # Si hay empates en primer puesto
        print('¡Empate!\nLos jugadores ')
        for x in range(empatados): print(f"{tabla[x]['nombre']}, ")
        print(f"con {tabla[0]['puntos']} puntos c/u.")
    else: print(f"¡El ganador es {tabla[0]['nombre']} con {tabla[0]['puntos']} puntos en {tabla[0]['tiros']} tiradas!") # Si no hay empates, imprimo al ganador


if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    print('¡Bienvenidso a Blackjack Python!\nIngrese cantidad de jugadores (Máximo 7):')
    while True:
        cant_jug = int(input())
        if 0 < cant_jug <= 7: break
        else: print('La cantidad de jugadores debe ser entre 1 y 7.')
    jugadores = crear_jugador(cant_jug) # Creo la lista de jugadores
    ronda = 'si' # Variable para chequear si quieren jugar mas rondas despúes
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