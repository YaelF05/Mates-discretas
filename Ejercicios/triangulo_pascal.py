"""

Escribe un programa en python que genere el triangulo de Pascal hasta n filas
@author: yaelf

"""
n = int(input("Ingrese un número: "))


if n <= 0:
    print("El número ingresado no es válido.")
else:
    fila_actual = [1]  
 
    for x in range(n - 1):
        fila_siguiente = [1]  
        for i in range(len(fila_actual) - 1):
            suma = fila_actual[i] + fila_actual[i + 1]  
            fila_siguiente.append(suma)
        fila_siguiente.append(1)  
        fila_actual = fila_siguiente

    print(' '.join(map(str, fila_actual)))  

