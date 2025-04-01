temp_fah = float(input("Ingresa la temperatura en F°:"))
#temp_cel = temp_fah - 32
#temp_cel = temp_cel * 5
#temp_cel = temp_cel / 9
#Es lo mismo que lo de abajo :)
temp_cel=( (temp_fah - 32) * 5) /9
temp_kelv = temp_cel + 273.15
print("Grados Celsius", round(temp_cel,2), "Grados Kelvin", round(temp_kelv,2))