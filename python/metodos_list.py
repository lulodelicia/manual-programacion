### METODOS DE LISTAS ###

"""
# METODO append()
## Añade un elemento al final de la lista

lista = ["felipe", "carlitos", "eugenia"]

lista.append("julieta")

print(lista)
"""


"""
# METODO clear()
## Elimina todos los elementos de una lista

lista = ["julieta", "luca", "felipe"]

lista.clear()

print(lista)
"""

"""
# METODO copy()
## Te devuelve todos los elementos de una lista

lista = ["pepe", "juan", "luca"]

otra_lista = lista.copy()

print(otra_lista)
print(lista)

"""
"""
# METODO count()
## Te devuelve cuantas veces esta repetido cierto elemento

frutas = ["manzana", "banana", "manzana"]

x = frutas.count("manzana")

print(x)
"""

"""
# METODO extend()
## el metodo sirve para unir dos listas
juegos = ["rayman", "fall guys", "cuphead"]

vb = ["fifa", "fornite"]

juegos.extend(vb)

print(juegos) 
"""

"""
#METODO index
## sirve para saber la posicion de un elemento

avengers = ["spider man", "thor", "ironman"]


x = avengers.index("ironman")

print(x)
"""

"""
#METODO insert
## sirve para agregar un elemento en la posicion que
## quieras

hola = ["hola ", "buen dia", "buenas noches"]

c = hola.insert(2, "buenas tardes")

print(c)
"""

"""
#METODO pop
## sirve para remover cosas de lista con el indice

cantantes = ["paulo", "camilo", "ice cube"]

cantantes.pop(1)

print(cantantes)
""" 

"""
#METODO remove
## sirve para remover un elemento de la lista

vocales = ["a", "e", "i", "o", "h"]

vocales.remove("h")

print(vocales)
"""

""" 
#METODO reverse
## sirve para dar vuelta la lista
numeros = ["1", "2", "3", "4"]

numeros.reverse()

print(numeros)
"""

"""
#METODO sort
## sirve para ordenar la lista

kl = ["hola", "buenas tardes", "buenas noches"]

kl.sort()

print(kl)

"""