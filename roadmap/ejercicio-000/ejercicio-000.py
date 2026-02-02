# ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
# - Recuerda que todas las instrucciones de participación están en el
#   repositorio de GitHub.
#
# Lo primero... ¿Ya has elegido un lenguaje?
# - No todos son iguales, pero sus fundamentos suelen ser comunes.
# - Este primer reto te servirá para familiarizarte con la forma de participar
#   enviando tus propias soluciones.
#
# EJERCICIO:
# - Crea un comentario en el código y coloca la URL del sitio web oficial del
#   lenguaje de programación que has seleccionado. [check]
# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una línea, varias...). [check]
# - Crea una variable (y una constante si el lenguaje lo soporta). [check]
# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...). [check]
# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" [check]
#
# ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
# debemos comenzar por el principio.

# --------------------------------------------------------------------------------------------------

# Vale, para crear comentarios en python es con el # (numeral)

"""
Existe esta otra manera, sin embargo no es recomendable, ya que al usarse de mala
manera puede cargarse en memoria, y hacer que haya mas peso en la ejecución del programa.
No es lo ideal. Por lo recomentable es usar # en cada linea de comentario. Este metodo
solo es usable al inicio de un modulo, o debajo de un def o un class para descripción.
De lo contrario es aplicar una mala practica que tiene como consecuencia cargar un
objeto inutil en memoria.
"""

# En python es facil declarar un variable.
x = "Hola mundo"

# Sin embargo para las constantes es diferente, ya que esto presisamente no existe.
# por lo que seria mas que todo por convicción:

NOMBRE_LENGUAJE = "python"

# Esto no quiere decir que python lo proteje y su valor no cambie, sino que esto seria
# mas aplicado de manera consciente y como buena practica.

# Python al no ser un lenguaje altamente tipado, no tiene una manera fija de como declarar
# tipos de datos, por lo que unicamente tendriamos lo siguiente

caracter = 'v'
cadena = "Velkez" # Las comillas dobles no influyen en nada, puede ser escrito con comillas simples o dobles, pero por ejntendimiento se puede aplicar así
alternativa = """ Esta puede ser otra alternativa
en la que se pues escribir
con saltos de linea """ # Pero este debe ser usado en casos muy especificos
entero = 25
numero_decimal = 3.1416
booleano = True # Este es peculiar, ya que si o si debe tener la letra en mayuscula (True/False)


# Por ultimo un agradeble saludo a nuestra nueva etapa,
# y al lenguaje que nos acompañará de aquí en adelante

saludo = "¡Hola Mundo! Y hola, Python"

print(saludo)
