n = int(input("Introduce un número entero: "))
suma = 0
lim = (n + 100)
i = n + 1
while (i <= lim):
    suma = suma + i
    i = i + 1

print("La suma de los 100 siguientes numeros de "+ str (n) +" es:", suma)
