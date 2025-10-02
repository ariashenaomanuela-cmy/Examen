# MANUELA ARIAS - 2025 
# Ejercicio: Números Camaleón

import random  # para generar numeros al azar

# pedir al usuario cuantos numeros quiere validar
cantidad = int(input("Cantidad de numeros a validar: "))

# lista para guardar los numeros que vamos a generar
numeros = []

# generar numeros aleatorios de 3 a 5 cifras
for i in range(cantidad):
    # randint elige un numero entre el minimo y el maximo
    num = random.randint(100, 99999)
    numeros.append(num)

# mostramos los numeros generados separados por coma
print("Números generados:", ", ".join(str(n) for n in numeros))

print("Resultados:")

# recorrer los numeros para ver si son camaleon
for num in numeros:
    # sacar la suma de los digitos
    suma = 0
    for d in str(num):  # recorrer el numero como texto
        suma += int(d)

    # invertir el numero (convertir a texto, dar vuelta y volver a numero)
    invertido = int(str(num)[::-1])

    # comprobar condiciones
    es_camaleon = False
    if suma % 2 == 0:  # si la suma es par
        if invertido % 3 == 0:  # y si el invertido es divisible entre 3
            es_camaleon = True

    # imprimir el resultado
    if es_camaleon:
        print(num, "-> Si (suma =", suma, "es par, invertido =", invertido, "divisible entre 3 -> Si)")
    else:
        print(num, "-> No (suma =", suma, ", invertido =", invertido, ")")
