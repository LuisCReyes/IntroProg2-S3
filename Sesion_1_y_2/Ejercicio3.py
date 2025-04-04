salario_bruto = float(input("Bienvenido a mi calculadora de salario neto:" ))
desc_renta = salario_bruto * 0.10
desc_seguro = salario_bruto * 0.05
Fond_pensiones = salario_bruto * 0.03
Sum_descuentos = desc_renta + desc_seguro + Fond_pensiones
salario_neto = salario_bruto - Sum_descuentos
print("------------------------------------------------------------------------------------------")
print("El salario bruto es: ", salario_bruto)
print("Los decuentos aplicados son: ", Sum_descuentos)
print("Su salario neto es: ", salario_neto)
print("------------------------------------------------------------------------------------------")