### Tarea Semana 2 Weekly Moodle ###

print("=== Sistema de Evaluación de Calificaciones ===")
print("Verifica si aprobó o reprobó")

# Calcular promedio de Calificaciones
print("Calcular promedio de Calificaciones")

# Solicitar y validar lista de Calificaciones separadas por comas
while True:
    try:
        entrada = input("Ingresa Calificaciones separadas por comas 0/100 ")
        Calificaciones = [float(x.strip()) for x in entrada.split(",")]
        if all(0 <= x <= 100 for x in Calificaciones) and len(Calificaciones) > 0:
            break
        else:
            print("Las Calificaciones deben estar entre 0 y 100 y la lista no puede estar vacía")
    except ValueError:
        print("Ingresa números válidos separados por comas: ")

# Calcular promedio usando un bucle for
Suma = 0
for Nota in Calificaciones:
    Suma += Nota
promedio = Suma / len(Calificaciones)
print(f"Calificaciones: {Calificaciones}")
print(f"Promedio: {promedio:.2f}")

if promedio >= 70:
    print("Aprobado, cumpliste tu deber xd ") 
else:
    print("Reprobado, debes prestar más atención  :c ")
# Cuenta Calificaciones mayores a un valor
print("======================================")
print("Valor de comparación de Calificaciones")
print("======================================")

# Solicitar y validar un valor para comparar
while True:
    try:
        valor = float(input("Calificaciones mayores a "))
        if 0 <= valor <= 100:
            break
        print("El valor debe estar entre 0 y 100")
    except ValueError:
        print("Ingrese un número valido")


# Contar Calificaciones mayores usando un bucle while
Contadormayor = 0
Iterona = 0
while Iterona < len(Calificaciones):
    if Calificaciones[Iterona] > valor:
        Contadormayor += 1
    Iterona += 1
print(f"Calificaciones mayores a {valor}: {Contadormayor} ")

# Parte 4: Buscar una calificación específica
print("======================================")
print("Buscar una calificación específica")
print("======================================")

# Solicitar y validar la calificación
while True:
    try:
        Valorbuscado = float(input("Ingresa la calificación que va a buscar: "))
        if 0 <= Valorbuscado <= 100:
            break
        print("La calificación debe estar entre 0 y 100 ")       
    except ValueError:
        print("Ingrese un número valido ")

# Verificar y contar la calificación usando for, break y continue
contador = 0
encontrada = False
for Nota in Calificaciones:
    if Nota == Valorbuscado:
        encontrada = True
        contador += 1
        continue  
    if encontrada and contador > 0:
        break  
if encontrada:
    print(f"La calificación {Valorbuscado} aparece {contador} veces ")
else:
    print(f"La calificación {Valorbuscado} no está en la lista ")
