print("🏰 ¡BIENVENIDO A LA MAZMORRA! 🏰")
print("Te despiertas en un lugar oscuro y frío.")
print("Frente a ti hay dos caminos")
print("El camino de la izquierda se ve a simple vista iluminado y muy colorido")
print("El camino de la derecha se ve tetrico y con muchas dificultades")

decision1 = input("¿Vas a la izquierda o a la derecha? ").lower()

if decision1 == "izquierda":

    print("Te confias por ser un camino facil, y caes en una trampa llegado a un nido de arañas venenosas") 

elif decision1 == "derecha":
    print("Caminas hacia la derecha y te encuentras un COFRE brillante.")

    decision2 = input("¿Quieres abrir el cofre? (si/no): ").lower()
    
    if decision2 == "si":
        print("Te encuentras con un botin muy bueno, como monedad de oro armadura buena y armas increibles")
    else:
        print("Te dio miedo y te fuiste a casa sin nada")

else:
    print("Te quedaste quieto y te comieron las ratas. Fin.")