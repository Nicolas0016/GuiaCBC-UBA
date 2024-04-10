# Importamos la librería random para barajar las cartas
import random

# Definimos el mazo con las cartas del 1 al 12, repitiendo el conjunto 4 veces
mazo = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12] * 4

# Barajamos las cartas del mazo
random.shuffle(mazo)

# Función para jugar al 7
def jugar(mazo, tope):

  puntuacion = 0  # Variable para almacenar la puntuación del jugador
  
  # Bucle que se ejecuta mientras la puntuación sea menor al tope
  while tope > puntuacion:
    # Se toma la última carta del mazo
    carta = mazo.pop()

    # Si la carta es mayor a 7, se suma 0.5 a la puntuación
    if carta > 7:
      puntuacion += 0.5
    # Si no, se suma el valor de la carta a la puntuación
    else:
      puntuacion += carta

  # Se retorna la puntuación final del jugador
  return puntuacion

# Simulamos el juego para dos jugadores
jugador_uno = jugar(mazo, 7.5) 
jugador_dos = jugar(mazo, 7.5)

# Imprimimos la puntuación de cada jugador
print(f"""
Puntuación Jugador 1: {jugador_uno}
Puntuación Jugador 2: {jugador_dos}
""")
