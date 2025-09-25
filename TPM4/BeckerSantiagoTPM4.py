#1
for i in range(101):
    print(i)

#2
num = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

#3
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
print("Suma:", sum(range(min(a, b) + 1, max(a, b))))

#4
suma = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
print("Total acumulado:", suma)

#5
import random
numero = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

#6
for i in range(100, -1, -2):
    print(i)

#7
n = int(input("Ingrese un número entero positivo: "))
print("Suma:", sum(range(n + 1)))

#8
pares = impares = negativos = positivos = 0
for i in range(100):
    n = int(input(f"Ingrese el número {i+1}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n < 0:
        negativos += 1
    elif n > 0:
        positivos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)

#9
suma = 0
for i in range(100):
    n = int(input(f"Ingrese el número {i+1}: "))
    suma += n
print("Media:", suma / 100)

#10
num = input("Ingrese un número: ")
print("Número invertido:", num[::-1])
