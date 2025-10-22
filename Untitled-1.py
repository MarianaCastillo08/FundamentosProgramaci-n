print("Ejemplo 1/n")
nombre="Mariana"
edad=17 
print("hola, soy Mariana")
print("tengo", edad, "años")


print("\nEjemplo 2\n")
print("hola mundo")
print("Hola\nMundo")
print("Línea 1\nLínea 2\nLínea 3")


print("\nEjemplo 3\n")
print("Nombre:\tMariana")
print("Edad:\t17") 
print("Ciudad:\tMonterrey")


print("\nEjemplo 4\n")
print("Ana:\tHola, ¿cómo estás?")
print("Luis:\tBien, ¿y tú")
print("Ana:\t¡Genial!\n")
print("===== Chat guardado en =====")
print("C:\\Users\\MARIANA_CASTILLO_VALDEZ\\Documents\\chat.txt") 


print("\nEjemplo 5\n")
print("Hola", "Mundo")
print("Me", "gusta", "dibujar")
print("Tengo", 1, "mascota en mi casa")
nombre = "Mariana"
cantidad_hermano = 1
print("Me dicen", nombre, "y tengo", cantidad_hermano, "hermano") 


print("Ejericio 6. OPERADORES ARITMÉRICOS")
numero1 = 42
numero2 = 22
suma = numero1 + numero2 
print("Operador suma:", suma) 
resta = numero1 - numero2 
print("Operador resta", resta)
multiplicacion = numero1 * numero2
print("Operador multiplicacion", multiplicacion)
division = numero1 / numero2
print("Operador division:", division)
division_entera = 10 // 3
print("Operador division entera:", division_entera)
residuo = 10 % 3
print("Operador residuo:", residuo)
potencia = 2 ** 3
print("Operador potencia:", potencia) 


print("Ejercicio 7. operadores de comparación")
print("¿He aprobado o no la materia?")
calificacion = 70
resultado5 = calificacion >= 70
print("¿Aprobé?:", resultado5)
resultado6 = calificacion > 70
print("¿Aprobé?:", resultado6)
mi_edad = 17
edad_minima = 18
resultado1 = mi_edad == 15
print("\n¿Soy mayor de edad? (==):", resultado1)
resultado2 = mi_edad != 20
print("¿tengo 18 años? (!=):", resultado2)
resultado3 = mi_edad < 18
print("¿Mi edad es menor que 18? (<):", resultado3)
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):", resultado4) 


print("Ejercicio 8. Operadores lógicos")
tengo_internet = True
tengo_cuenta = True
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar? (ambas True):", puedo_jugar)
tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Puedo jugar? (una es False):", puedo_jugar2)
tengo_celular = True
tengo_tablet = False 
tengo_diapositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menos una True):",tengo_diapositivo)
esta_lloviendo = False 
puedo_salir = not esta_lloviendo 
print("¿Puedo salir? (NOT False = True):",puedo_salir) 


print("Ejercicio 9. Operadores de asignación\n")
puntos = 0
print("Puntos iniciales:", puntos)
puntos += 10
print("Ganaste 10 puntos (+=):", puntos)
puntos -= 5
print("Perdiste 5 puntos (-=):", puntos)
puntos *= 2
print("¡Puntos x2! (*=):", puntos)
puntos /= 2
print("Dividir puntos (/=):", puntos) 


print("Ejercicio 10. Operadores de identidad\n")
print("=== ¿SON LA MISMA COSA? ===")
lista1 = ["manzana", "pera"]
lista2 = ["manzana", "pera"]
lista3 = lista1
print("¿lista1 es lista2? (is):", lista1 is lista2)
print("¿lista1 es lista3? (is):", lista1 is lista3)
print("¿lista NO es lista2? (is not):", lista1 is not lista2) 