import random

"""
Adivina el numero

Projecto: crear un programa que pida al usuario adivinar un numero entre 1 y n, donde el usario elige n. 
"""



def juego_de_adivinar(n):
    # Pedirle al usuario rango de numeros para adivinar
    # n = int (input("Ingresa rango de numeros por adivinar: "))
    number_to_guess = random.randint(1, n)

    not_guessed = True 
    guesses = 0
    while not_guessed:
        # Pedirle al usuario numero por adivinar
        guess = int (input("Ingresa tu numero por adivinar: "))

        # adivino muy abajo
        if guess < number_to_guess:
            print ("adivino muy abajo")
        # adivino muy arriba
        if guess > number_to_guess:
            print ("adivino muy arriba")
        # adivino bien
        if guess == number_to_guess:
            print ("adivino bien")
            not_guessed = False
    
n=10        
juego_de_adivinar(n)


print(f'te tomo este numero de intentos: {guesses}')
