import sqlite3 
def crear_base_datos():
    conexion = sqlite3.connect("casino.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            saldo REAL NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()
    print("¡Base de datos y tabla 'usuarios' creadas con exito!")
if __name__ == "__main__":
    crear_base_datos()
