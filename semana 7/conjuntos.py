# Los conjuntos son incambiables/inmodificables (item)
# son no ordenados
# no permiten duplicados
# son iterables
# se construyen usando llaves {}
# si permite agregar o eliminar items

usuarios = {"user1", "user2", "user3", "user4"}

# usuarios[1] = "usern" no se puede editar items

usuarios.add("user5")

print(usuarios)

#se puede validar si un elemento exite o no en un conjunto
print("user2" in usuarios)
print("user6" in usuarios)

#se puede remover elementos
usuarios.discard("user3")
print(usuarios)

# for i in usuarios:
#     print(i)

usuariosNuevos = {"user6", "user7"}

usuarios.union(usuariosNuevos)

# for i in usuarios:
#     print(i)

otrosUsuarios = {"user1", "user3", "user9", "user8", "user7"}
usuarios.update(otrosUsuarios)

for i in usuarios:
    print(i)
