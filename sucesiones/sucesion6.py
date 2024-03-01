"""
Created on Thu Feb 29 19:01:47 2024

@author: Yael Franco
"""

numero = int(input("Ingresa un número: "))

for i in range(1, numero + 1):
    numerador = (-1)**(i-1) * (i - 1)
    print((-1)**(i-1) * (i - 1), "/", i)

