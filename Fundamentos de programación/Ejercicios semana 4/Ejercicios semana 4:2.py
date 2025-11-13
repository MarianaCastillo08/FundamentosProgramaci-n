print("\nEjercicio 1\n")
canciones = ["As It Was", "Flowers", "Vampire", "Cruel summer", "Calm Down"]

print("MIS CANCIONES FAVORITAS")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])


print("\nEjercicio 2\n")
amigos = []

print("Lista inicial:", amigos)

amigos.append("Andrea")
print("Después de agregar a Andrea:", amigos)

amigos.append("Meli")
print("Después de agregar a Meli:", amigos)

amigos.append("Xime:")
print("Después de agregar a Xime:", amigos)

print(f"\nTotal de amigos: {len(amigos)}") 


print("\nEjercicio 3\n")
calificaciones = [98, 90, 88, 92, 89]

print("Tus calificaciones:", calificaciones)

suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Promedio: {promedio}")

mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor califiación: {mejor}")
print(f"Peor calificación: {peor}")


print("\nEjercicio 4\n")
carrito = []

print("Agregando productos al carrito...")
carrito.append("iPhone 15")
carrito.append("AirPods")
carrito.append("Funda")
carrito.append("Cargador")

print("Carrito actual:", carrito)
print(f"Productos en el carrito:{len(carrito)}")

print("\n Eliminando la funda...")
carrito.remove("Funda")

print("Carrito final:", carrito)
print(f"Total de productos: {len(carrito)}")


print("\nEjercicio 5\n")
videojuegos = ["Minecraft", "Fortnite", "Valorant", "Roblox", "GTA V"]

print("MI TOP 5 VIDEOJUEGOS:")
print(videojuegos)

print(f"\nMi favorito (posición 0): {videojuegos[0]}")
print(f"El de la posición 5 (último): {videojuegos[-1]}")

print("\n Cambio de opinión...")
videojuegos[0] = "Apex Legends"

print("Top 5 actualizado:")
print(videojuegos)


print("\nEjercicio 6\n")
series = ["Stranger Things", "Wednesday", "The Last of Us"]

print("Series para ver:", series)

series.append("One Piece")
print("Agregaste One Piece:", series)

if "Wednesday" in series:
    print("\nSi tienes Wednesay en tu lista")

if "Breaking Bad" in series:
    print("Tienes Breaking Bad")
else:
    print("No tienes Breaking Bad en tu lista")

print(f"\n¡Terminaste de ver {series[0]}!")
series.pop(0)
print("Series restantes:", series)