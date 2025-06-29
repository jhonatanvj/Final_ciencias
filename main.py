from database import JSONDatabase

db = JSONDatabase()

while True:
    print("\n1. Insertar\n2. Buscar\n3. Listar todo\n4. Actualizar\n5. Salir")
    op = input("Elige una opción: ")
    
    if op == '1':
        key = input("Clave: ")
        name = input("Nombre: ")
        edad = input("Edad: ")
        db.insert(key, {"nombre": name, "edad": edad})
        print("Insertado")
    
    elif op == '2':
        key = input("Clave: ")
        data = db.get(key)
        print("Resultado:", data if data else "No encontrado")
    
    elif op == '3':
        print("Registros:")
        for item in db.list_all():
            print(item)

    elif op == '4':
        key = input("Clave a actualizar: ")
        name = input("Nuevo nombre: ")
        edad = input("Nueva edad: ")
        db.update(key, {"nombre": name, "edad": edad})
        print("Actualizado")

    elif op == '5':
        break
