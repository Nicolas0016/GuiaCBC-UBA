from random import randint

# Función para simular el llenado del álbum por un usuario
def simularLlenado(cantidadFiguritas):
    # Creamos un álbum vacío representado por una lista de ceros
    albumUsuario = [0] * cantidadFiguritas
    intentos = 0  # Contador de intentos

    # Mientras el álbum no esté completo
    while sum(albumUsuario) != len(albumUsuario):
        # Generamos una figurita aleatoria
        figurita = randint(0, cantidadFiguritas - 1)
        # Colocamos la figurita en el álbum del usuario
        albumUsuario[figurita] = 1
        intentos += 1  # Incrementamos el contador de intentos
    return intentos

# Función para simular el llenado del álbum por múltiples usuarios
def simulacion(cantidadPersonas):
    vecesSimuladas = 0
    datosTomados = []

    # Realizamos la simulación para la cantidad especificada de personas
    while vecesSimuladas < cantidadPersonas:
        datosTomados.append(simularLlenado(6))  # Simulamos el llenado del álbum para un usuario
        vecesSimuladas += 1  # Incrementamos el contador de simulaciones
    return datosTomados

# Función para mostrar los resultados de la simulación
def mostrarResultados():
    usuario = 0
    usuarios = simulacion(6)  # Simulamos el llenado del álbum para 6 personas
    # Iteramos sobre los resultados de cada usuario
    while usuario < len(usuarios):
        print("Usuario", usuario, "compró:", usuarios[usuario], "paquetes")
        usuario += 1  # Pasamos al siguiente usuario
    # Calculamos y mostramos el promedio de paquetes comprados por todas las personas
    print("El promedio fue del: ", sum(usuarios) / len(usuarios))
    # NO HACE FALTA USAR ROUND; TODAVIA NO LO APRENDEMOS

# Llamamos a la función para mostrar los resultados de la simulación
mostrarResultados()

'''
1. Hacer un programa que simule el llenado de un álbum dinámicamente:
Se asigna la tarea de crear un programa que simule el llenado de un álbum de figuritas
y calcule el promedio entre múltiples personas. 
'''
