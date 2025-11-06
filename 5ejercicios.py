print("\nEJERCICIO 1: TABLA DE MULTIPLICAR")

numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


print("\nEJERCICIO 2")

numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
    print(f"La suma total es: {suma}")


print("\nEJERCICIO 3")
texto = "Hola, ¿cómo están?"
contador = 0
for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1
print(f"Hay {contador} vocales")


print("\nEJERCICIO 4")

numeros = [15, 42, 8, 23, 67, 31]
mayor = numeros [0]
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es: {mayor}")


print("\nEJERCICIO 5")

cuadrados = []
for i in range(1, 6):
    cuadrados.appendi(i ** 2)
print(cuadrados)