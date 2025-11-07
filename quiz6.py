#Pide al usuario dos números enteros a y b (a <= b) e imprime todos los números primos entre a y b, uno por línea.

# Pedimos los valores al usuario
a = int(input("Introduce el primer número debe ser >= al segundo numero(a): "))
b = int(input("Introduce el segundo número (b): "))

# Verificamos que a <= b
if a > b:
    print("El primer número debe ser menor o igual que el segundo.")
else:
    print("Números primos entre {a} y {b}:")
    
    # Recorremos todos los números del rango
    for num in range(a, b + 1):
        if num > 1:  # Los primos son mayores que 1
            es_primo = True
            # Verificamos si tiene divisores
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(num)
