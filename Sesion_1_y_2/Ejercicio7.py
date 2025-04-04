precio_ori = float(input("Porfavor ingrese el precio del producto: \n"))
por_desc = float(input("Ingrese el descuento a aplicar: \n"))
multp = precio_ori * por_desc
descuento = (multp /100) 
precio_desc = precio_ori -descuento
iva = float(input("Ingrese el IVA: "))
precio_IVA = precio_desc * iva
precio_IVA /= 100
precio_f = iva + precio_desc
print(f"El producto tiene un precio de: {precio_ori: .2f}, con un descuento aplicado de: {por_desc: .2f}, el producto con el descuento tendría un costo de: {precio_desc: .2f}, \n con el IVA de: {iva: .2f}, el producto tendrá el costo final de: {precio_f: .2f}")