print("Ejercicio 1\n")

canciones_dia = ("Blindings Lights", "Heat Waves", "Anti-Hero")
canciones_noche = ("Leviating", "As It Was")

playlist_completa = canciones_dia + canciones_noche
print(canciones_dia)
print(canciones_noche)
print(playlist_completa)


print("Ejercicio 2\n")
ubicaciones_norte = ((19.5, -99.2), (19.6, -99.3))
ubicaciones_sur = ((19.4, -99.1), (19.3, -99.4))

todas_unicaciones = ubicaciones_norte + ubicaciones_sur
print(ubicaciones_norte)
print(ubicaciones_sur)
print(todas_unicaciones, "\n")


print("Ejercicio 3 - Repetición\n")

emojis = ("🦋", "🤍")
cartel = emojis * 5
print(emojis)
print(cartel, "\n")


print("\Ejercicio 4 - Longitud\n")

seguidores_tiktok = 1500
seguidores_insta = 2300
seguidores_fb = 950
seguidores_total = seguidores_tiktok + seguidores_insta + seguidores_fb
seguidores = (seguidores_tiktok, seguidores_insta, seguidores_fb)
cantidad_redes = len(seguidores)

print("Seguidores en TikTok:", seguidores_tiktok)
print("Seguidores en Instagram:", seguidores_insta)
print("Seguidores en Facebook:", seguidores_fb)
print("Total de seguidores:", seguidores_total)
print("Cnatidad de redes sociales:", cantidad_redes)


print("\nEjercicio 5 - count\n")

resultados_partidas = ("gané", "perdí", "gané", "gané", "perdí", "gané", "empate")
veces_gane = resultados_partidas.count("gané")
print("He ganado:", veces_gane)


print("\nEjercicio 6 - inex\n")

ranking = ("Marcelo", "Mariana", "Vane", "Abi", "Fer", "Marcelo", "Orlando")
mi_posición = ranking.index("Mariana")
print("Estoy en la posición: ", mi_posición, "\n")