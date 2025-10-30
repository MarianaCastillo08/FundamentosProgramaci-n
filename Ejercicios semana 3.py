Edad = int(input("ingresa tu edad:  "))
if Edad >= 16:
    print("puedes jugar")
else:
    print("eres muy joven para este juego")


calificación = int(input("Ingresa tu calificación (0-100):  "))
if calificación >= 90 and calificación <= 100:
    print("Excelente")
elif calificación >= 70 and calificación < 90:
    print("Aprobado")
elif calificación >= 0 and calificación < 70:
    print("Ay!, no aprobado")
else:
    print("Calificación inválida")


    edad = int(input("¿Cuál es tu edad"))
    genero = input("¿Cuál es tu genero favorito? (accion, comedia, terror): ").lower()

    if edad < 13:
        print("Te recomendamos películas infantiles")

    elif edad >= 13 and edad <= 17 and genero == "acción":
        print("Te recomendamos: Spider-Man (PG-13)")
    
    elif edad >= 13 and edad <= 17 and genero == "comedia":
        print("Te recomendamos: Shrek (PG-13)")

    elif edad >= 13 and edad <= 17 and genero == "terror":
        print("Te recomendamos: Scary Stories (PG-13)")

    elif edad >= 18 and genero == "acción":
        print("Te recomendamos: Jhon Wick")
    
    elif edad >= 18 and genero == "comedia":
        print("Te recomendamos: Superbad")

    elif edad >= 18 and genero =="terror":
        print("Te recomendamos: El Conjuro") 