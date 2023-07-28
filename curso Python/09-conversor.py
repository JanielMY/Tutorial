Temperatura = float(input ("Ingresa temperatura:"))
escala = input ("Es Fahrenheit(F) o es Celsius(C)?:").lower()

if escala ==  "f":
   celsius = (Temperatura - 32) * 5/9
   print(celsius)
elif escala == "c":
   fahrenheit = Temperatura * 1.8 + 32
   print(fahrenheit) 
else:
   print ("escala incorrecta")