"""
Created on Tue Mar  5 16:41:18 2024

@author: Yael Franco
"""

generacion = int(input("Ingresa un número: "))
antepasados = 2
total_antepasados = 0

for i in range (1, generacion + 1):
    total_antepasados += antepasados**i
    print(f"La cantidad de antepasados de la generación {i} son: {total_antepasados}")