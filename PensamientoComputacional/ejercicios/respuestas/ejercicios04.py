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
    cantidad_a_comprar  = 11
    cantidad_albunes = 0 
    usuarios = simulacion(6)  # Simulamos el llenado del álbum para 6 personas
    # Iteramos sobre los resultados de cada usuario
    while usuario < len(usuarios):
        print("Usuario", usuario, "compró:", usuarios[usuario], "paquetes")
        
        if cantidad_a_comprar <= usuarios[usuario]:
            cantidad_albunes = cantidad_albunes + 1 
        usuario += 1  # Pasamos al siguiente usuario
    # NO HACE FALTA USAR ROUND; TODAVIA NO LO APRENDEMOS
    print("la probabilidad que llenes el album con:", cantidad_a_comprar, "es del:",round((cantidad_albunes / len(usuarios))*100, 2), "%", "o", cantidad_albunes, "/", len(usuarios))

# Llamamos a la función para mostrar los resultados de la simulación
mostrarResultados()



"""Establecer un valor máximo para la cantidad de figuritas que el usuario puede comprar (11): 
Para promover la práctica de la lógica condicional, se propuso limitar la cantidad máxima de figuritas
que un usuario puede comprar en una sola transacción. Esta restricción fomenta la planificación y toma
de decisiones en el diseño del programa."""