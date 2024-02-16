"""
Created on Thu Feb 15 17:08:36 2024

@author: yaelf
"""

numero = int(input("Escribe un número: ")) 

if numero == 1:
    print("El número 1 no es primo")
    while numero <= 1:
        numero = int(input("Escribe de nuevo un número: "))

for i in range (2, numero + 1 ):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
    
if primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
