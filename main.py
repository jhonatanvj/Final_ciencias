from database import JSONDatabase

bd = JSONDatabase()

while True:
    print("""
1. Insertar objeto
2. Buscar objeto por clave
3. Listar todos los objetos
4. Actualizar objeto
5. Eliminar objeto
6. Salir""")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        clave = input("Clave del objeto: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        bd.insertar(clave, {"nombre": nombre, "edad": edad})
        print("Objeto insertado exitosamente.")
    elif opcion == '2':
        clave = input("Clave a buscar: ")
        resultado = bd.obtener(clave)
        print("Resultado:", resultado if resultado else "No encontrado")
    elif opcion == '3':
        for item in bd.listar():
            print(item)
    elif opcion == '4':
        clave = input("Clave del objeto a actualizar: ")
        nombre = input("Nuevo nombre: ")
        edad = input("Nueva edad: ")
        bd.actualizar(clave, {"nombre": nombre, "edad": edad})
        print("Objeto actualizado.")
    elif opcion == '5':
        clave = input("Clave del objeto a eliminar: ")
        bd.eliminar(clave)
        print("Objeto eliminado.")
    elif opcion == '6':
        break
    else:
        print("Opción no válida.")
