print("Ejercicio 1 con while")

contador_numero = 1

while contador_numero <= 5:
    print(f"Número: {contador_numero}")
    contador_numero = contador_numero + 1 


    print("\nEjercicio 2 con while - cuenta regresiva")
    numero = 5

    while numero > 0:
        print(f"Faltan {numero} segundos...")
        numero = numero - 1

        print("¡Despegue!")


    print("\nEjercicio 3 con while - suma acumulativa")
    numeros = 1
    suma = 0

    while numeros <= 50:
        suma = suma + numeros
        numeros = numeros + 1

        print(f"La suma del 1 al 50 es: {suma}\n")


        print("\nEjercicio 4 - Tabla de multiplicar")
        multiplicador = 1

        while multiplicador <= 10:
            resultado = 7 * multiplicador
            print(f"7 x {multiplicador} = {multiplicador}")
            multiplicador = multiplicador + 1

        print("¡Tabla completa! \n")


        print("\nEjercicio 5 - Numero pares del 2 al 50")
        numeros_pares = 2

        while numeros_pares <= 50:
            print(f"Número par: {numeros_pares}")
            numeros_pares = numeros_pares + 2

        print("¡Todos los pares mostrados!\n")


        print("\nEjercicio 6 - Dividir un número a la mitad")
        numero_a_dividir = 100

        while numero_a_dividir >= 1:
            print(f"Número actual: {numero_a_dividir}")
            numero_a_dividir = numero_a_dividir / 2

        print(f"Número final (menor a 1): {numero_a_dividir}") 