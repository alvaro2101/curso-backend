import sqlite3

# Función para GUARDAR datos (Create)
def registrar_jugador(nombre, saldo):
    # 1. Conectar
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    
    # 2. Insertar
    # OJO: Usamos '?' en lugar de poner las variables directamente. 
    # Esto es una buena práctica de seguridad (evita hackeos básicos).
    cursor.execute("INSERT INTO usuarios (nombre, saldo) VALUES (?, ?)", (nombre, saldo))
    
    # 3. Guardar cambios y cerrar
    conexion.commit()
    conexion.close()
    print(f"✅ Jugador '{nombre}' registrado con ${saldo}.")

# Función para LEER datos (Read)
def ver_jugadores():
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    
    # 1. Consultar
    cursor.execute("SELECT * FROM usuarios")
    
    # 2. Traer los resultados
    # fetchall() significa "tráeme todo lo que encontraste"
    todos_los_usuarios = cursor.fetchall()
    
    conexion.close()
    
    print("\n--- 📋 LISTA DE JUGADORES EN LA BD ---")
    for usuario in todos_los_usuarios:
        # usuario es una tupla: (id, nombre, saldo)
        print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Saldo: ${usuario[2]}")

# --- ZONA DE EJECUCIÓN ---
if __name__ == "__main__":
    # Vamos a crear dos jugadores de prueba
    registrar_jugador("Alvaro", 15500)
    registrar_jugador("Mary", 1000) # ¡Ella siempre gana! 😉
    registrar_jugador("David", 750)
    
    # Y ahora leemos la base de datos para ver si se guardaron
    ver_jugadores()
    # Función para ACTUALIZAR (Update) - Por ejemplo, si ganan o pierden
def actualizar_saldo(id_usuario, nuevo_saldo):
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    
    # Actualizamos el campo 'saldo' DONDE el id coincida
    cursor.execute("UPDATE usuarios SET saldo = ? WHERE id = ?", (nuevo_saldo, id_usuario))
    
    conexion.commit()
    conexion.close()
    print(f"🔄 Saldo del usuario {id_usuario} actualizado a ${nuevo_saldo}.")

# Función para BORRAR (Delete) - Si el usuario elimina su cuenta
def eliminar_usuario(id_usuario):
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    
    # Borramos la fila DONDE el id coincida
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    
    conexion.commit()
    conexion.close()
    print(f"❌ Usuario {id_usuario} eliminado de la base de datos.")
if __name__ == "__main__":
    # Primero miramos quiénes están
    ver_jugadores()
    
    # --- ZONA DE HACKEO ---
    id_a_hackear = 1      # <--- Asegúrate que este sea TU ID
    monto_millonario = 1000000
    
    # Ejecutamos el hack
    actualizar_saldo(id_a_hackear, monto_millonario)
    
    # Verificamos si funcionó
    print("\n--- DESPUÉS DEL HACKEO ---")
    ver_jugadores()