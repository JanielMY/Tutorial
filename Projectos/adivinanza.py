import random

"""
Adivina el numero

Projecto: crear un programa que pida al usuario adivinar un numero entre 1 y n, donde el usario elige n. 
"""

# Pedirle al usuario rango de numeros para adivinar
n = int(input("Ingresa rango de numeros por adivinar: "))
number_to_guess = random.randint(1, n)

# Pedirle al usuario numero por adivinar
guess = input("Ingresa tu numero por adivinar: ")

