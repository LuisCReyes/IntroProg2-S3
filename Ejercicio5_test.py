def conversion_tiempo(segundos_totales):
    # Conversión de segundos a horas, minutos y segundos
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    
    return horas, minutos, segundos

total_segundos = int(input("Por favor introduce la cantidad total de segundos: "))
horas, minutos, segundos = conversion_tiempo(total_segundos)
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")