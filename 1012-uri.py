value = input().split(" ")
a,b,c = value
pi = 3.14159
triangulo = (float(a)*(float(c)))/2
circulo = pi*(float(c)*(float(c)))
trapezo = float(c)*(float(a)+float(b))/2
quadrado = float(b)*float(b)
rectangulo = float(a)*float(b)

print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZO: %.3f\nQUADRADO: %.3f\nRECTANGULO: %.3f3"%(triangulo,circulo,trapezo,quadrado,rectangulo))