import math
a = int(input("Introduce un número entero: "))
b = int(input("Introduce un número entero: "))
c = int(input("Introduce un número entero: "))
r1 = (b**2 - (4*a*c))


if r1 <= 0 :
    print ("no tiene resultado")
else:
    r2 = 2*a
    if  r2 == 0 :
       print ("no tiene resultado")
    else:
        r3 = ((b*-1) + math.sqrt(r1)) / r2
        r4 = ((b*-1) - math.sqrt(r1)) / r2
        print (f"el resultado es: {r3} y {r4}")
