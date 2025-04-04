print("Bienvenido 🥰")
primer_tramo = float(input("Ingrese la duración del primer tramo de vuelo: "))
primer_escala = float(input("Ingrese la duración de la primera escala: "))
segundo_tramo = float(input("Ingrese la duración del segundo tramo de vuelo: "))
segunda_escala = float(input("Ingrese la duración de la segunda escala: "))
tercer_tramo = float(input("Ingrese la duración del tercer tramo de vuelo: "))

#Sumna de las escalas
Sum1 = primer_tramo + primer_escala
Sum2 = segundo_tramo + Sum1
Sum3 = Sum2 + segunda_escala
Sum_vuelo = Sum3 + tercer_tramo

print("----------------------------------------------------------------------------------")
print("El tiempo total del vuelo es de: ", Sum_vuelo, "Horas")
print("----------------------------------------------------------------------------------")