"""
Created on Thu Feb 15 17:46:04 2024

@author: yaelf
"""

numero = int(input("Ingresa un número: "))

divisor = 2
while numero > 1:
    while numero % divisor == 0:
        print(divisor, end=" ")
        numero //= divisor
    divisor += 1
