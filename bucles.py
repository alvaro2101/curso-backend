# Empezamos con la mochila vacía
mochila = []

opcion = ""

# El menú se repetirá hasta que escribas "salir"
while opcion != "salir":
    print("-------------------------")
    print("🎒 TU MOCHILA TIENE: " + str(len(mochila)) + " objetos.")
    print("1. Agregar objeto")
    print("2. Ver mochila")
    print("Escribe 'salir' para terminar.")
    
    opcion = input("¿Qué quieres hacer? (1/2/salir): ").lower()

    if opcion == "1":
        nuevo_item = input("¿Qué encontraste?: ")
        # .append() sirve para AGREGAR cosas al final de la lista
        mochila.append(nuevo_item) 
        print("✅ ¡" + nuevo_item + " guardado!")

    elif opcion == "2":
        print("--- CONTENIDO ---")
        for item in mochila:
            print("- " + item)
            
    elif opcion == "salir":
        print("Cerrando mochila... ¡Adiós!")
        
    else:
        print("Opción no válida. Intenta de nuevo.")