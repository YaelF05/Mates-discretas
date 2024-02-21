"""

Escribe un programa en python que diga si un número es perfecto
Escribe un programa que imprima todos los números perfectos hasta N
@author: yaelf

"""
numero = int(input("Escribe un número: "))

print (" ")

print(f"Los números perfectos hasta {numero} son:")
for i in range(1, numero + 1):
    suma = 0
    for j in range(1, i):
        if i % j == 0:
            suma += j
    if suma == i:
        print(i)

if suma == numero:
    print(f"El número {numero} es un número perfecto")
else:
    print(f"El número {numero} no es un número perfecto")