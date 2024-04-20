from random import shuffle

# Función para mezclar el mazo de cartas
def mezclar_mazo(): 
    MAZO = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12] * 4
    shuffle(MAZO)
    return MAZO

# Función para determinar el resultado de una partida
def resultado(MAZO, tope):
    resultado = 0 
    while resultado < tope:
        carta = MAZO.pop(0)
        if MAZO == []:
            MAZO = mezclar_mazo()  # Si el mazo está vacío, se vuelve a mezclar
        if carta > 7: 
            resultado += 0.5  # Si la carta es mayor que 7, suma 0.5 al resultado
        else:
            resultado += carta  # Si la carta es 7 o menor, suma el valor de la carta al resultado
    return resultado

# Función para jugar una partida para cada jugador
def jugar_partida(MAZO, cant_personas):
    i = 0
    resultados = [0] * cant_personas
    estrategia = [5, 5.5, 6, 6.5, 7]  # Estrategias de cada jugador
    while i < cant_personas:
        resultados[i] = resultado(MAZO, estrategia[i])  # Se determina el resultado para cada jugador
        i += 1
    return resultados

# Función para simular un evento con un número de intentos
def simular_evento(intentos, MAZO, cant_personas):
    i = 0
    datos = [0] * intentos
    while i < intentos:
        datos[i] = jugar_partida(MAZO(), cant_personas)  # Se juega la partida y se registran los resultados
        i += 1
    return datos

# Función para contar las veces que un jugador gana con un resultado de 7
def veces_ganadas(numero_intentos, CANTIDAD_JUGADORES):
    datos  = simular_evento(numero_intentos, mezclar_mazo, CANTIDAD_JUGADORES)
    recorrido_datos = 0
    veces_ganadas = [0] * CANTIDAD_JUGADORES  # Inicialización de la lista de veces ganadas

    while recorrido_datos < len(datos):
        i = 0 
        while i < (len(datos[recorrido_datos])):
            if datos[recorrido_datos][i] == 7:
                veces_ganadas[i] += 1  # Se incrementa el contador de victorias si el resultado es 7
            i += 1
        recorrido_datos += 1

    return veces_ganadas

# Función para calcular el promedio de victorias de cada jugador
def sacar_promedio():
    numero_intentos = 1000
    CANTIDAD_JUGADORES = 5
    promedios = [0]*CANTIDAD_JUGADORES
    lista_ganadores = veces_ganadas(numero_intentos, CANTIDAD_JUGADORES)
    
    i = 0
    while i < len(lista_ganadores):
        promedios[i] = round((lista_ganadores[i]/sum(lista_ganadores))*100,2)  # Se calcula el promedio de victorias
        i = i + 1 
    return promedios


[print(f"la probabilidad de ganar con la estrategia {num_extrategia+1} es de: {promedio}%")
 for [num_extrategia, promedio] in enumerate(sacar_promedio())]
