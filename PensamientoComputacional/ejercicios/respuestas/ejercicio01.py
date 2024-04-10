def intentosRealizados():
  from random import randint

  # Lista para almacenar las figuritas del álbum
  albunUsuario = []

  # Contador de intentos
  intentos = 0

  # Bucle que se repite hasta que se completen las 7 figuritas del álbum
  while len(albunUsuario) <= 6:

    # Se genera un número aleatorio entre 0 y 6
    numero_figurita = randint(0, 6)

    # Si la figurita ya está en el álbum, se ignora
    if numero_figurita in albunUsuario:
      pass

    # Si la figurita no está en el álbum, se agrega 
    else:
      albunUsuario.append(numero_figurita)
    # Se aumenta el contador de intentos
    intentos = intentos +  1

  # Se retorna la cantidad de intentos realizados
  return intentos

# Se ejecuta la función y se imprime el resultado
print(intentosRealizados())