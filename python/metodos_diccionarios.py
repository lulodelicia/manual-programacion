### METODOS DE DICCIONARIO ###

"""
# METODO clear()
## Elimina todos los elementos del diccionario

dic = {
    "color":"rojo",
    "estatura":180
}

dic.clear()

print(dic)
"""

"""
# METODO copy()
## Devuelve una copia del diccionario

dic = {
    "color":"rojo",
    "estatura":180
}

dic_copy = dic.copy

print(dic_copy)
print(dic)
"""

"""
# METODO fromkeys()
## Crea un diccionario a partir de una lista y un solo valor

x = ['key1', 'key2', 'key3']

y = 0

diccionario = dict.fromkeys(x, y)

print(diccionario)
"""

"""
# METODO get()
## Te devuelve el valor de la clave que vos le digas

dic = {
    "color":"rojo",
    "estatura":180
}

x = dic.get("color")

print(x)
"""

"""
# METODO keys()
## Te devuleve una lista de las claves del diccionario

dic = {
    "color":"rojo",
    "estatura":180
}

key = dic.keys()

print(key)
"""

"""
# METODO pop()
## Sirve para eliminar determinado par clave-valor

dic = {
    "color":"rojo",
    "estatura":180
}

dic.pop('color')

print(dic)
"""

"""
# METODO popitem()
## Elimina el ultimo elemento del diccionario

dic = {
    "color":"rojo",
    "estatura":180
}

dic.popitem()

print(dic)
"""

"""
# METODO values()
## Devuelve una lista de los valores del diccionario

dic = {
    "color":"rojo",
    "estatura":180
}

val = dic.values()

print(val)
"""