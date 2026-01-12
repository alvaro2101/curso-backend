import random

print("🤖: He pensado un número secreto del 1 al 100.")
print("🤖: ¿Podrás adivinarlo?")

secreto = random.randint(1, 100)

mi_numero = 0
intentos = 0


while mi_numero != secreto:
    
 
    entrada = input("Adivina el número: ")
    
    if entrada.isdigit():
        mi_numero = int(entrada)
        intentos = intentos + 1 
        
        if mi_numero < secreto:
            print("🔼 ¡Más ALTO! (Tu número es muy pequeño)")
        elif mi_numero > secreto:
            print("🔽 ¡Más BAJO! (Te pasaste)")
        else:
            print("🎉 ¡CORRECTO! ¡Lo adivinaste!")
    else:
        print("⚠️ Por favor, escribe un número válido.")


print("--------------------------------")
print("Te tomó " + str(intentos) + " intentos ganar.")
print("--------------------------------")