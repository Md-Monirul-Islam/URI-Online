''''
Programer : Md.Monirul Islam Munna
'''
import cmath
value = input().split(' ')
a = float(value[0])
b = float(value[1])
c = float(value[2])
d = (b * b) - (4 * a * c)
if d<0 or a==0:
    print("Impossivel calcular")
else:
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print("R1 =%.5f"%sol1)
    print("R2 =%.5f"%sol2)