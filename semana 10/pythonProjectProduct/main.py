import pyodbc

# Conectarse a la base de datos SQL Server
server = '127.0.0.1'
database = 'producto'
username = 'root'
password = ''

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Función para listar productos
def listar_productos():
    cursor.execute('SELECT * FROM Productos')
    for row in cursor:
        print(row)

# Función para crear un producto
def crear_producto():
    nombre = input('Nombre del producto: ')
    tipo = input('Tipo de producto: ')
    precio = float(input('Precio del producto: '))
    descripcion = input('Descripción del producto: ')
    stock = int(input('Cantidad en stock: ')

    cursor.execute("INSERT INTO Productos (Nombre, Tipo, Precio, Descripcion, Stock) VALUES (?, ?, ?, ?, ?)",
                   (nombre, tipo, precio, descripcion, stock))
    conn.commit()
    print('Producto creado con éxito.')

# Función para eliminar un producto por nombre
def eliminar_producto():
    nombre = input('Nombre del producto a eliminar: ')
    cursor.execute("DELETE FROM Productos WHERE Nombre = ?", (nombre,))
    conn.commit()
    print(f'Producto "{nombre}" eliminado.')

# Menú principal
while True:
    print("\nOpciones:")
    print("1. Listar productos")
    print("2. Crear producto")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        listar_productos()
    elif opcion == "2":
        crear_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Cerrar la conexión a la base de datos
conn.close()
