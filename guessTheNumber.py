import random

numero = int(input("ingrese un número del 1 al 10: "))
numeroAleatorio = random.randint(1, 10)

if numero == numeroAleatorio:   
    print("Felicidades! Has adivinado el numero")
else:
    print("Suerte para la proxima")
    