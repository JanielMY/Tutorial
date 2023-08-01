# Tarea para Agosto 1, 2023

## Tipos de variables (para leer)

- [int](https://ellibrodepython.com/entero-en-python)
- [boolean](https://ellibrodepython.com/booleano-python)
- [float](https://ellibrodepython.com/float-python)
- [strings](https://ellibrodepython.com/cadenas-python)

### Ejercicos

#### Suma de dos enteros

```{python}
# Escribe un programa que solicite al usuario dos números enteros e imprima la suma de ambos.
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
suma = num1 + num2
print("La suma de los números es:", suma)
```

#### Producto de tres enteros

```{python}
# Escribe un programa que tome tres números enteros y calcule su producto.
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
producto = num1 * num2 * num3
print("El producto de los números es:", producto)

```
#### División de dos enteros

```(Python)
    # Escribe un programa que tome dos números enteros y calcule la división entera del primero entre el segundo.
    num1 = int(input("Ingrese el numerador: "))
    num2 = int(input("Ingrese el denominador: "))
    division = num1 // num2
    print("La división entera de los números es:", division)
```

### Ejercicios para el tipo boolean

#### Comparación de dos números

```{python}

# Escribe un programa que tome dos números y devuelva True si el primero es mayor que el segundo, y False en caso contrario.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
es_mayor = num1 > num2
print("El primer número es mayor que el segundo:", es_mayor)
```
#### Operaciones booleanas

```{Python}

# Escribe un programa que tome dos valores booleanos y devuelva el resultado de aplicar la operación AND y OR entre ellos.
valor1 = bool(input("Ingrese el primer valor booleano (True/False): "))
valor2 = bool(input("Ingrese el segundo valor booleano (True/False): "))
print("AND:", valor1 and valor2)
print("OR:", valor1 or valor2)
```

#### Evaluación de condiciones

```{python}

    # Escribe un programa que tome un número entero y devuelva True si es par, y False en caso contrario.
    numero = int(input("Ingrese un número entero: "))
    es_par = numero % 2 == 0
    print("El número es par:", es_par)
```

### Ejercicios para el tipo float

#### Calculo del área de un círculo

```{python}
# Escribe un programa que tome el radio de un círculo y calcule su área. (Utiliza la constante pi = 3.1416)
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
print("El área del círculo es:", area)
```

#### Conversión de grados Fahrenheit a Celsius

```{python}
# Escribe un programa que tome una temperatura en grados Fahrenheit y la convierta a grados Celsius.
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("La temperatura en grados Celsius es:", celsius)
```

#### Cálculo de la hipotenusa de un triángulo rectángulo

```{python}
# Escribe un programa que tome los catetos de un triángulo rectángulo y calcule su hipotenusa.
cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print("La hipotenusa del triángulo es:", hipotenusa)
```

### Ejercicios para el tipo strings

#### Concatenación de dos strings

```{python}
# Escribe un programa que tome dos cadenas y las concatene.
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
concatenacion = cadena1 + " " + cadena2
print("La concatenación de las cadenas es:", concatenacion)
```

#### Longitud de un string

```{python}
# Escribe un programa que tome una cadena y devuelva su longitud.
cadena = input("Ingrese una cadena: ")
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)
```

#### Inversión de un string

```{python}
# Escribe un programa que tome una cadena y la devuelva invertida.
cadena = input("Ingrese una cadena: ")
invertida = cadena[::-1]
print("La cadena invertida es:", invertida)
```
