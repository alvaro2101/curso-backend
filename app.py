print("--- SISTEMA DE SEGURIDAD TIPO ODISEA ---")
#ODISEA es una empresa de seguridad en mi pais
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("ACCESO CONCEDIDO")
    print("Bienvenido , " + nombre + ". Puedes pasar a la xona VIP.")
else:
    print("ACCESO DENEGADO")
    print("Los siento " + nombre + ", eres menor de edad.")
    faltan = 18 - edad
    print("Vuelve en " + str(faltan)+ "años.")

    print("--- Fin del Programa causa ---")