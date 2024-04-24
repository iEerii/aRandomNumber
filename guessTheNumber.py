import random

print("ADIVINA EL NUMERO QUE ESTOY PENSANDO")

numeroAleatorio = random.randint(1, 10)

while True:
    numero = int(input("Ingrese un número del 1 al 10: "))

    if numero <= 0 or numero > 10:
        print("Te dije del 1 al 10, gracioso. Vuelve a intentarlo")
    elif numero != numeroAleatorio:   
        print("Suerte para la proxima. Intentalo de nuevo")
    else:
        print("Felicidades! Has adivinado el numero")
        break
    
