#tuplas son colecciones de datos idénticos o distintos clasificados con un índice y que no pueden ser modificados.

#como se crea una tupla
colores = ("amarillo","azul", "rojo")
print(colores)

#se puden creat tuplas con un solo elemento, pero es importante dejar una coma (,) despues del elemento, de lo contrario el programa no lo reconocerá como una tupla, sino que asumirá que es una cadena con parentesis

color = ("verde",)
print(color)

# se pueden tener tuplas con cadena de textos, numeros, booleanos y mixtos

#se puede seleccionar un elemento de un tupla
animales = ("perro", "gato", "ratón")
print(animales[1])

#se puede aplicar slicing en las tuplas
otros_animales = ("perro", "gato", "ratón", "serpiente", "caballo")
print(animales[1:3])

#se puede determinar la longitud de una tupla
print(len(colores))

#Modificar una tupla de Python: Las Python tuples son inalterables, por lo que no pueden ser dotadas de nuevos elementos. Sin embargo, para actualizar una tupla ya existente, puedes crear una tupla y añadir valores nuevos además de la tupla original. Esto se hace con el operador +

algunos_animales = ("perro", "gato", "ratón", "serpiente", "caballo")
todos_los_animales = algunos_animales + ("hámster", "jirafa")
print(todos_los_animales)

#Convertir una tupla de Python en lista: Sin embargo, si hay valores de una tupla que no están actualizados, el método explicado anteriormente no te servirá. Como no puedes cambiar los valores que contiene una tupla de Python, necesitas una alternativa. Para este caso, lo mejor es la lista clásica. Al convertir una tupla en lista puedes volver a cambiar sus valores. Esto se hace de la siguiente manera;

juegos = ("mario", "GOW", "TR", "Genshin Impac", "Honkai Starlight")
lista_juegos = list(juegos)
lista_juegos[2] = "TRIII"
print(lista_juegos)

#Convertir una lista en tupla de Python: Este proceso también puede hacerse a la inversa. Si has creado una lista y quieres mantener sus valores en su forma actual, puedes convertir dicha lista en una tupla. En el siguiente ejemplo convertimos una lista en tupla y luego consultamos el tipo de dato de la tupla de Python por seguridad;

lista_video_juegos = ["TR", "TR II", "TR III", "TR IV"]
video_juegos = tuple(lista_video_juegos)
print(video_juegos)
print(type(video_juegos))

#funcion index
print(video_juegos.index("TR"))

#funcion count
print(video_juegos.count("TR"))