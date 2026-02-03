
# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

# _______________________________________________________________________________________

# OPERACIONES ARITMÉTICAS

first_number = 10
second_number = 4

suma = first_number + second_number
print(f"La suma de {first_number} mas {second_number} es igual a {suma} \n")

resta = first_number - second_number
print(f"La resta de {first_number} menos {second_number} es igual a {resta} \n")

multiplicacion = first_number * second_number
print(f"La multiplicación de {first_number} por {second_number} es igual a {multiplicacion} \n")

division_float = first_number / second_number
print(f"La división de {first_number} sobre {second_number} es igual a {division_float} en flotantes \n")

division_int = first_number // second_number
print(f"La división de {first_number} sobre {second_number} es igual a {division_float} en enteros \n")

modulo = first_number % second_number
print(f"El módulo de {first_number} de {second_number} es igual a {modulo} \n")

potencia = first_number ** second_number
print(f"La potencia de {first_number} elevado a {second_number} es igual a {potencia} \n")

# OPERACIONES DE ASIGNACIÓN

x = 12
print(f"x es igual a { x } (x = 12) \n")

x += 1
print(f"Ahora x es igual a { x } (x += 1) \n")

x -= 1
print(f"Sin embargo x volvio a ser igual a { x } (x -= 1) \n")

x *= 2
print(f"Ahora x multiplico su valor a { x } (x *= 2) \n")

x //= 2
print(f"Sin embargo lo devolvemos a su valor inicial { x } (x /= 2) \n")

x **= 2
print(f"Ahora x elevo su valor { x } (x **= 2) \n")

x %= 2
print(f"Ahora se comprobó que el valor anterior es { 'par' if x == 0 else 'impar' } por que el modulo es igual a {x} \n")

# OPERACIONES DE COMPARACIÓN

x = 12
y = 16

# ==: igual a
print(f"¿{ x } es igual a { y }? \n { x == y } \n")

# !=: diferente a
print(f"¿{ x } es distinto a { y }? \n { x != y } \n")

# >: mayor que
print(f"¿{ x } es mayor a { y }? \n { x > y } \n")

# <: menor que
print(f"¿{ x } es menor a { y }? \n { x < y } \n")

# >=: mayor o igual que
print(f"¿{ x } es mayor o igual a { y }? \n { x >= y } \n")

# <=: menor o igual que
print(f"¿{ x } es menor o igual a { y }? \n { x <= y } \n")

# OPERADORES LÓGICOS

# and: las dos condiciones se deben cumplir
print(f"12 es igual a 6 por 2 y 4 es par \n { 12 == 6 * 2 and 4 % 2 == 0 } \n")

# or: alguna de las dos condiciones de debe cumplir
print(f"12 es igual a 6 por 2 o 4 es impar \n { 12 == 6 * 2 or 4 % 2 == 0 } \n")

# not: unicamente funciona en condiciones negando la condición
print(f"si 12 es igual a 2 por 6, { 'no es igual' if not 12 == 2 * 6 else 'si es igual' } \n")

# OPERADOR DE IDENTIDAD

x = "naranja"

print(f"{ 'es un tuberculo' if x is 'patatas' else 'es otro alimento' } \n")
print(f"{ 'es otro alimento' if x is not 'patatas' else 'es un tuberculo' } \n")

# OPERADORES DE PERTENENCIA

x = 12
y = [ 1, 2, 3, 4 ]

print(f"{ x } esta en { y }? \n { x in y } \n")
print(f"{ x } no esta en { y }? \n { x not in y }")

conquest = 'es un tuberculo' if x is 'patatas' else 'es otro alimento'


# El ternario lo use varias cosas, es mas, en operadores de identidad se uso.
# 'es un tuberculo' if x is 'patatas' else 'es otro alimento'
# sin embargo, en este operador no es permitido usar el operador is, sino ==.
# Y lo mismo con is not, siendo != la manera correcta de hacerlo.