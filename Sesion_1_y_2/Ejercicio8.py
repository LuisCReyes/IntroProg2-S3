import os
def menu():
    print("Por favor seleccione la moneda a la que desea convertir:")
    print("1. Euros")
    print("2. Libras")
    print("3. Yenes")
    print("4. Salir")

def convertir_dolares_a_euros(dolares, tasa_cambio_euros):
    euros = dolares * tasa_cambio_euros
    print(f"{dolares:.2f} dólares son {euros:.2f} euros.")
    return euros

def convertir_dolares_a_libras(dolares, tasa_cambio_libras):
    libras = dolares * tasa_cambio_libras
    print(f"{dolares:.2f} dólares son {libras:.2f} libras.")
    return libras

def convertir_dolares_a_yenes(dolares, tasa_cambio_yen):
    yenes = dolares * tasa_cambio_yen
    print(f"{dolares:.2f} dólares son {yenes:.2f} yenes.")
    return yenes

def main():
    print("Bienvenido al convertidor de divisas")
    while True:
        dolares = float(input("Ingrese la cantidad de dólares: "))
        tasa_cambio_euros = 0.91
        tasa_cambio_libras = 0.78
        tasa_cambio_yen = 145.53

        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            convertir_dolares_a_euros(dolares, tasa_cambio_euros)
            press_key = input("--- Presione una tecla para continuar ----")
            os.system("cls || clear")
        elif opcion == 2:
            convertir_dolares_a_libras(dolares, tasa_cambio_libras)
            press_key = input("--- Presione una tecla para continuar ----")
            os.system("cls || clear")
        elif opcion == 3:
            convertir_dolares_a_yenes(dolares, tasa_cambio_yen)
            press_key = input("--- Presione una tecla para continuar ----")
            os.system("cls || clear")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            os.system("cls || clear")

if __name__ == "__main__":
    main()