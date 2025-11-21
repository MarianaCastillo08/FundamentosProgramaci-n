# Ejercicio 1: CONVERTIR TEXTO A NÚMERO // JUEVES

print("Ejercicio 1: Convertir texto a número\n")

try:
    edad = int(input("¿Cuántos años tienes? "))
    print(f"El próximo año tendrás {edad + 1}")
except ValueError:
    print("ERROR: Debes escribir un número, no texto")

# EJERCICIO 2: DIVISIÓN ENTRE NÚMEROS \\ JUEVES

print("Ejercicio 2: División entre números\n")

try:
    numero1 = int(input("Escribe el primer numero: "))
    numero2 = int(input("Escribe el segundo número: "))
    resukltado = numero1 / numero2
    print(f"El resultado de {numero1} / {numero2} = {resultado}")
except ZeroDivisionError:
    print("Error: Debes escribir números, no texto")
    

# EJERCICIO 3: ACCEDER A ELEMENTOS DE UNA LISTA // JUEVES

print("Ejercicio 3: Acceder a elementos  de una lista2")
try:
    amigos = ["Juan", "María", "Carlos", "Sofía"]
    posicion = int(input("cuál es el número de amigo que quieres ver? (1-4): "))
    # Restamos 1 porque las listas empiezan en 0
    amigo = amigos [posicion - 1]
    print(f"Tu amigo es: {amigo}")
except IndexError:
    print("ERROR: Ese número no existe en la lista")
except ValueError:
    print("ERROR: Debes escribir un número")


# EJERCICIO 4: BUSCAR RN UN DICCIONARIO // JUEVES 

print("Ejercicio 5: Buscar en un diccionario")
try:
    telefonos = {
        "Ethan": "555-1234",
        "Evan": "555-5678",
        "SHIZU": "555-9012"
    }

    nombre = input("¿De quien quieres el telefono? ")
    telefono = telefonos[nombre]
    print(f"El telefono de {nombre} es: {telefono}")
except: KeyError
print("ERROR: Ese nombre no esta en la agenda")


# EJERCICIO 5: MULTIPLICAR NÚMERO POR TEXTO // JUEVES

print("Ejercicio 5: Multiplicar número por texto")
try:
    numero = int(input("¿Cuántas veces quieres ver el mensaje?: "))
    mensaje = input("¿Cuál es el mensaje?: ")
    print(mensaje * numero)
except ValueError:
    print("ERROR: Debes escribir un número entero")
except TypeError:
    print("ERROR: No se puede hacer esa operación")


# EJERCICIO 6: VALIDAR EDAD PARA ENTRAR A LA PELI // JUEVES

print("Ejercicio 6: Validar edad para entrar a una peli")
try:
    edad = int(input("¿Cuantos años tienes?"))
    if edad < 0:
        print("ERROR: La edad no puede ser negativa")
    elif edad < 13:
        print("Puedes ver peliculas infantiles (G)")
    elif edad < 16:
        print("Puedes ver peliculas para adolescentes (PG-13)")
    elif edad < 18:
        print("Puedes ver peliculas de +!5 (PG-15)")
    else:
        print("Puedes vere cualquier pelicula; incluyendo mayores de 18")
    except ValueError:
        Print("ERROR: Debes escribir tu edad como tu numero")



