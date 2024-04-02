# Teoría de conjuntos 
La teoría de conjuntos es un área fundamental de las matemáticas que trata sobre las propiedades y relaciones entre conjuntos, que son colecciones bien definidas de objetos. Python, como un lenguaje de programación versátil, ofrece varias fromas de trabajar conjuntos y aplicar conceptos de teoría de conjuntos.

## Creación de conjuntos 
En python, puedes crear un conjunto utilizando llaves {} o la funciión set()


```python
A = {1, 2, 3, 4, 5}
```


```python
B = {3, 4, 5, 6, 7}
```


```python
C = set([3, 6, 9, 12, 15])
```

## Listas vs conjuntos


```python
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```


```python
lista
```




    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]




```python
conjunto = set(lista)
```


```python
conjunto
```




    {1, 2, 3, 4, 5}



## Operaciones 
 Python proporciona operadores y métodos para realizar operaciones básicas de conjuntos como unión, intersección, diferencia y diferencia simétrica.

## Unión 
La unión de conjuntos es correspondiente la unificación de los elementos de dos conjunbtos o incluso más conjuntos, que pueden partiendo de esto conformar una nueva forma de conjunto, en la cual los elementos dentro de este correspondan a los elementos de los conjuntos originales. Cuando un elemento es repetido, forma parte del conjunto unión una vez sólamente; esto difiere de la unión de conjuntos en la concepción tradicional de la suma, en la cual los elementos comunes se consideran tantas veces como se encuentren en la totalidad de los conjuntos.

Formalmente, si A y B son conjuntos, la unión de A y B se define como el conjunto C que contiene todos los elementos que pertenecen a A, a B, o ambos. Mateáticamente, esto se puede expresar como:

$$
    C = A \cup B = {x:x \in A  \quad o \quad x \in B}
$$

En python, la opereación de unión puede realizarse utilizando el operador | o el método union()


```python
A | B 
```




    {1, 2, 3, 4, 5, 6, 7}




```python
A.union(B)
```




    {1, 2, 3, 4, 5, 6, 7}



## Intersección 

La intersección de conjuntos es una operación que devuelve un nuevo conjunto que contiene únicamente los elementos comunes a dos o más conjuntos. Es decir, se seleccionan aquellos elementos que están presentes en todos los conjuntos involucrados en la operación de intersección.

Por ejemplo: dados los conjuntos R = {1,2,3,4} y el conjunto S = {3,4,5,6}, podríamos decir que la intersección seria:
 S {3,4}
 
 $$ 
     C = A \cap B = x:x \in  A y x \in B
 $$
 
 


```python
A & B
```




    {3, 4, 5}




```python

```


```python

```
