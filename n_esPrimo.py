"""
@author: yaelf
"""

numero = int(input("Escribe un número: "))

primo = True 

while numero <= 1:
    print("El número debe ser un entero mayor que uno")
    numero = int(input("Vuelva a escribir un número: "))


for i in range (2, numero // 2 + 1 ):
    if numero % i == 0:
        primo = False
        break
    
if primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
