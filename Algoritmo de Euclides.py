"""
Created on Fri Feb 16 12:24:02 2024

@author: zS23017346
"""

numero1 = int(input('Ingresa el primer número:'))
numero2 = int(input('Ingresa el segundo número:'))

while numero2 != 0:
    residuo = numero1 % numero2 
    numero1 = numero2
    numero2 = residuo
    
print(f"El máximo común divisor es {numero1}")