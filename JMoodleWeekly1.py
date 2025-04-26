#### Nombre del producto ###

nombre = input("¿Qué compraste? ")
if not nombre.strip():
    print("Que nombre tan raro xd ") 
    exit()

### Precio  ###

precio = input("¿Cuánto cuesta cada uno? $Platica ")
if precio.isnumeric() or (precio.replace(".", "").isnumeric() and precio.count(".") <= 1):
    precio = float(precio)
    if precio <= 0:
        print("¿Gratis? no creo")
        exit()
else:
    print("¿Eso es un número? Nope, intenta de nuevo xd")
    exit()

### Cantidad ###

cantidad = input("¿Cuántos llevas? ")
if cantidad.isnumeric():
    cantidad = int(cantidad)
    if cantidad <= 0:
        print("Como que nada? xd")
        exit()
else:
    print("Ojala fueran numeros validos xd")
    exit()

### Descuento ###

descuento = input("¿Porcentaje de descuento? ")
if descuento.isnumeric():
    descuento = float(descuento)
    if descuento < 0 or descuento > 100:
        print("Y Ese descuento tan raro xd")
        exit()
else:
    print("Eso no es un porcentaje valido xd")
    exit()

### Cálculo del costo###

CostoSdescuento = precio * cantidad
if descuento > 0:
    print(f"Se te descuentan un {descuento}%!")
    Costototal = CostoSdescuento * (1 - descuento / 100)
else:
    print("Sin descuento, qué triste xd")
    Costototal = CostoSdescuento

### Mostrar resultado ###

print(f"Producto: {nombre}, Cantidad: {cantidad} Precio/U ${precio:.2f} Descuento: {descuento}%")
print(f"Costo total: ${Costototal:.2f}")
if Costototal == 0:
    print("¿La ganga")
elif Costototal > 10000:
    print("Eso son varias horas de camello xd")
elif Costototal > 5000:
    print("Worth la vdd?")
