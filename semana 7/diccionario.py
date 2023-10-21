#diccionarios estan compuestas de clave valor
#son mutables
#los diccionarios no admiten claves en espicial claves repetidas
#desde python 3.7 los diccionarios son ordenados

user1 = {"name": "Juan", "lastname": "Castro", "email": "jcastro@mail.com"}

#podemos ver la longitud
print(len(user1))

#podemos ver el tipo
print(type(user1))

#podemos agregar nuevos elementos
user1["pass"] = "qwert"

print(user1.keys())

print(user1.items())

#podemos optener un elemento en especifico

print(user1.get("name"))

#para remover

user1.pop("email")
print(user1.items())

user1.popitem()
print(user1.items())

print(user1.get("password"))

#podemos usar for para imprimir el diccionario, ya sea solo claves, solo valores o ambos

#acceso a clave y valor
for x,y in user1.items():
    print(x,y)

#acceso a clave
for x in user1.keys():
    print(x)

#acceso a valores
for y in user1.values():
    print(y)


#diccionarios de diccionarios
user2 = {"name": "Ana", "lastname": "torre", "email": "atorre@mail.com", "pass": "1234"}
user3 = {"name": "Erre", "lastname": "Malave", "email": "emalave@mail.com", "pass": "1234"}
user4 = {"name": "Sebas", "lastname": "Chavez", "email": "schavez@mail.com", "pass": "1234"}

users = {"user2": user2, "user3": user3, "user4": user4}
print(users)

print(users["user2"]["lastname"])

##ejercicios usando diccionarios y funciones en el que se cree un producto con las siguientes claves:
#id, nombre, costo, cantidad, margen_ganancia
#se deben almacenar los productos con dos campos adicionales que son calculados PV = costo/(1-mg)
#valor del inventario, invt = cantidad * costo
#almacenar los productos creados en un diccionario de diccionarios
#la app debe permitir iniciar, mostrar un menu 1. agregar propucto, 2. listar los productos