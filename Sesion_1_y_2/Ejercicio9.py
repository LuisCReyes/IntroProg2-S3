#Calculo del tiempo total de una película con comerciales
duracion_peli = int(input("Ingrese la duración de la película en minutos: "))
prev_comerciales = int(input("Ingrese la duración de los comerciales previos a la película en minutos: "))
pausas_comerciales = int(input("Ingrese la cantidad de los comerciales durante la película en minutos: "))
dura_pausa_comerciales = int(input("Ingrese la duración de las pausas comerciales en minutos: "))
total_comerciales = pausas_comerciales * dura_pausa_comerciales
duración_total = duracion_peli + prev_comerciales + total_comerciales
print(f"La duración original de la pelicula es de {duracion_peli} minutos, los comerciales tendrán una duración de {total_comerciales} minutos, \n en total la proyección tendrá una duración de: {duración_total} minutos.")