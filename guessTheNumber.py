import random

numeroAleatorio = random.randint(1, 10)

while True:
    numero = int(input("ingrese un número del 1 al 10: "))

    if numero != numeroAleatorio:   
        print("Suerte para la proxima. Intentalo de nuevo")
    else:
        print("Felicidades! Has adivinado el numero")
        break
