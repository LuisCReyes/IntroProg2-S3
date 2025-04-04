#Conversión de unidades de tiempo
total_segundos = int(input("Porfavor introduce la cantidad total de segundos: "))
tiempo_horas = total_segundos // 3600
multp = total_segundos - (tiempo_horas * 3600) #No funciona, no da los minutos
tiempo_minutos = multp // 60 #No funciona, no da los minutos
Restar = multp - (tiempo_minutos * 60) #No funciona, no da los segundos restantes
print(tiempo_horas, "horas", tiempo_minutos, "minutos", Restar, "segundos")