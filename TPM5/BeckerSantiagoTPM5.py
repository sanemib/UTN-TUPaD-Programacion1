#1
notas = [int(input(f"Ingrese nota {i+1}: ")) for i in range(10)]
print("Notas:", notas)
print("Promedio:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#2
productos = [input(f"Ingrese producto {i+1}: ") for i in range(5)]
print("Lista ordenada:", sorted(productos))
eliminar = input("Producto a eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
print("Lista actualizada:", productos)

#3
import random
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Números:", numeros)
print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))

#4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = list(set(datos))
print("Lista sin repetidos:", sin_repetidos)

#5
alumnos = [input(f"Ingrese nombre de alumno {i+1}: ") for i in range(8)]
accion = input("¿Desea agregar (A) o eliminar (E) un alumno?: ").upper()
if accion == "A":
    alumnos.append(input("Nombre a agregar: "))
elif accion == "E":
    nombre = input("Nombre a eliminar: ")
    if nombre in alumnos:
        alumnos.remove(nombre)
print("Lista final de alumnos:", alumnos)

#6
numeros7 = [int(input(f"Ingrese número {i+1}: ")) for i in range(7)]
print("Lista original:", numeros7)
numeros7 = [numeros7[-1]] + numeros7[:-1]
print("Lista rotada:", numeros7)

#7
temps = [[int(input(f"Min día {i+1}: ")), int(input(f"Max día {i+1}: "))] for i in range(7)]
prom_min = sum(t[0] for t in temps) / 7
prom_max = sum(t[1] for t in temps) / 7
amplitudes = [t[1] - t[0] for t in temps]
dia_mayor_amp = amplitudes.index(max(amplitudes)) + 1
print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)
print("Día mayor amplitud:", dia_mayor_amp)

#8
notas = [[int(input(f"Nota estudiante {i+1}, materia {j+1}: ")) for j in range(3)] for i in range(5)]
prom_estudiantes = [sum(fila)/3 for fila in notas]
prom_materias = [sum(notas[i][j] for i in range(5))/5 for j in range(3)]
print("Promedio por estudiante:", prom_estudiantes)
print("Promedio por materia:", prom_materias)

#9
tablero = [["-" for _ in range(3)] for _ in range(3)]
for turno in range(9):
    for fila in tablero:
        print(" ".join(fila))
    jugador = "X" if turno % 2 == 0 else "O"
    f, c = map(int, input(f"Jugador {jugador}, ingrese fila y columna: ").split())
    if tablero[f][c] == "-":
        tablero[f][c] = jugador
    else:
        print("Casilla ocupada, turno perdido.")
for fila in tablero:
    print(" ".join(fila))

#10
ventas = [[int(input(f"Ventas producto {i+1}, día {j+1}: ")) for j in range(7)] for i in range(4)]
totales_productos = [sum(fila) for fila in ventas]
totales_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = totales_dias.index(max(totales_dias)) + 1
producto_max = totales_productos.index(max(totales_productos)) + 1
print("Total por producto:", totales_productos)
print("Día con mayores ventas:", dia_max)
print("Producto más vendido:", producto_max)
