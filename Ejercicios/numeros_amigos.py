"""
Escribe un programa en python que indique si dos números dados son amigos
@author: yaelf

"""
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

suma1 = 0
suma2 = 0

for i in range (1,numero1):
    if numero1 % i == 0:
        suma1 += i
           
for i in range (1,numero2):
    if numero2 % i == 0:
        suma2 += i
        
if suma1 == numero2 and suma2 == numero1:
    print(f"El {numero1} y el {numero2} son números amigos")
else:
    print(f"El {numero1} y el {numero2} no son números amigos")