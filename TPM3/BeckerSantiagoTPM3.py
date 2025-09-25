#1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#2
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5
contrasena = input("Ingrese una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
mi_moda = mode(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)
mi_media = mean(numeros_aleatorios)

print("Números:", numeros_aleatorios)
print("Moda:", mi_moda)
print("Mediana:", mi_mediana)
print("Media:", mi_media)

# Determinar sesgo
if mi_media > mi_mediana > mi_moda:
    print("Sesgo positivo o a la derecha")
elif mi_media < mi_mediana < mi_moda:
    print("Sesgo negativo o a la izquierda")
elif mi_media == mi_mediana == mi_moda:
    print("Sin sesgo")
else:
    print("La distribución no cumple exactamente con un sesgo definido")

7#
texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
    
print(texto)

#8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10
def obtener_estacion(hemisferio, mes, dia):
    # Convertimos la fecha a un número comparable en formato MMDD
    fecha = mes * 100 + dia

    if hemisferio.upper() == 'N':  # Hemisferio norte
        if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
            return "Invierno"
        elif 321 <= fecha <= 620:
            return "Primavera"
        elif 621 <= fecha <= 920:
            return "Verano"
        elif 921 <= fecha <= 1220:
            return "Otoño"
    elif hemisferio.upper() == 'S':  # Hemisferio sur
        if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
            return "Verano"
        elif 321 <= fecha <= 620:
            return "Otoño"
        elif 621 <= fecha <= 920:
            return "Invierno"
        elif 921 <= fecha <= 1220:
            return "Primavera"
    else:
        return "Hemisferio no válido"

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Obtener y mostrar estación
estacion = obtener_estacion(hemisferio, mes, dia)
print(f"La estación del año es: {estacion}")
