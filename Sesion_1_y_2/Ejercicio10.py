#Cálculo del volumen de un cilindro y su área superficial
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))
pi = 3.1416
área = (radio * radio) * pi
volumen = área * altura
area_lat = 2 * pi * radio * altura
area_total = area_lat + (2 * área)
area_superficial = area_total
print(f"El área superficial de un cilindro con radio {radio:.2f}, con una altura de {altura:.2f}, tiene un volumen de {volumen:.2f} y un área superficial de {area_superficial:.2f}.")
