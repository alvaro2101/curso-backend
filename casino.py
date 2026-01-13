import random
import sqlite3
def iniciar_sesion(nombre_jugador):
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, saldo FROM usuarios WHERE nombre = ?",(nombre_jugador,))
    usuario = cursor.fetchone()
    if usuario:
        id_usuario, saldo = usuario
        print(f"\n👋 ¡Bienvenido de nuevo, {nombre_jugador}!Tienes ${saldo}.")
    else:
        saldo = 250 
        cursor.execute("INSERT INTO usuarios (nombre, saldo) VALUES (?, ?)",(nombre_jugador, saldo))
        conexion.commit()
        id_usuario = cursor.lastrowid
        print(f"\n✨¡Hola {nombre_jugador}! Cuenta creada con bono de ${saldo}.")
    conexion.close()
    return id_usuario, saldo
def guardar_progreso(id_usuario, nuevo_saldo):
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET saldo = ? WHERE id = ?", (nuevo_saldo, id_usuario))
    conexion.commit()
    conexion.close()

print("🎰 BIENVENIDO AL CASINO DE ADIVINANZAS 🎰")
print("🤖: He pensado un número secreto del 1 al 100.")
print("💰: Cada intento cuesta $10. Si ganas, recibes $100.")

# 1. Pedimos nombre y cargamos la base de datos
nombre = input("Ingresa tu nombre de jugador: ")
id_jugador, saldo = iniciar_sesion(nombre)

secreto = random.randint(1, 100)
mi_numero =0
intentos =0
intentos = 0

# --- AQUÍ EMPIEZA EL BUCLE (Faltaba esta línea) ---
while mi_numero != secreto:
    
    # 2. Verificamos si tiene dinero para seguir jugando
    if saldo < 10:
        print("\n🚫 ¡Te quedaste sin dinero! No puedes seguir adivinando.")
        break # Rompemos el ciclo si no hay plata

    entrada = input("\nAdivina el número: ")
    
    # ... el resto de tu código sigue aquí ...

    if entrada.isdigit():
        mi_numero = int(entrada)
        intentos = intentos + 1
        
        # 3. COBRAMOS EL INTENTO Y GUARDAMOS EN LA BD
        saldo = saldo - 10 
        guardar_progreso(id_jugador, saldo)
        print(f"   💸 Costo de intento: -$10 | Saldo actual: ${saldo}")

        if mi_numero < secreto:
            print("🔼 ¡Más ALTO!")
        elif mi_numero > secreto:
            print("🔽 ¡Más BAJO!")
        else:
            # 4. SI GANA, DAMOS EL PREMIO Y GUARDAMOS
            print(f"🎉 ¡CORRECTO! ¡Lo adivinaste en {intentos} intentos!")
            saldo = saldo + 100
            guardar_progreso(id_jugador, saldo)
            print(f"🏆 ¡Ganaste $100! Tu saldo final es: ${saldo}")
            
    else:
        print("⚠️ Por favor, escribe un número válido.")

print("---------------------------")
print("Fin del juego.")