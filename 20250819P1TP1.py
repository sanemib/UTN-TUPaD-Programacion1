# 1
print ("Hola Mundo")

# 2
nombre = input('Ingrese su nombre:')
print (f"Hola {nombre} !")

# 3
nombre = input('Ingrese su nombre:')
apellido = input('Ingrese su apellido:')
edad = input('Ingrese su edad:')
residencia = input('Ingrese su lugar de residencia:')
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4
import math
radio = float(input("Ingrese el radio del circulo:"))
area =  math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print (f"El area es: {area} y el perimetro es: {perimetro}")

# 5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6
numero = int(input("Ingresa un número: "))
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print("\nResultados:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division:.2f}")
else:
    print("Error: Ambos números deben ser distintos de 0.")

# 8
peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))
imc = peso / ((altura) ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

# 10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números ingresados es: {promedio}")
