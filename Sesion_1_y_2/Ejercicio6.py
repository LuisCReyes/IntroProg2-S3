Peso_kg = float(input("Ingrese su peso en kg: "))
Altura_metros = float(input("Ingrese su altura en metros: "))
Altura_metros = Altura_metros * Altura_metros
imc = Peso_kg / Altura_metros
imc *= 100
resultado = imc / 100

if imc < 18.5:
    print("Usted está bajo de peso")
elif imc < 24.9:
    print("Su peso normal")
elif imc < 29.9:
    print("Usted tiene sobrepeso")
else:
    print("Usted tiene obesidad")
    #Clasificación del IMC en adultos 
#IMC menor a 18.5: Bajo peso
#IMC entre 18.5 y 24.9: Peso normal
#IMC entre 25.0 y 29.9: Sobrepeso
#IMC de 30.0 o más: Obesidad

print(f"Peso ingresado: {Peso_kg:.2f} kg, Altura ingresada: {Altura_metros:.2f} metros, IMC: {resultado:.2f}")
