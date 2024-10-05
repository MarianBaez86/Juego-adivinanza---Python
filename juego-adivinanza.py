import random


numero_secreto = random.randint(0,100)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print("¡Bienvenido a adivinan el juego del número secret!")

while not adivinado and cant_intentos < cant_max_intentos:
    if not cant_intentos < cant_max_intentos:
        print("¡Game over! No has podido adivinar dentro de los 5 intentos")
        break
    
    numero = int(input("Intoduce un número del 0 al 99: "))

    if numero == numero_secreto:
        print("¡Felecitaciones has adivinado el número secreto!")
        adivinado= True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")

    cant_intentos += 1

