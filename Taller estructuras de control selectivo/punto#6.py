"""
Entradas:
ValorA-->int-->A
ValorB-->int-->B
ValorC-->int-->C
ValorD-->int-->D
Salidas:
valor-->str->v
"""
datos = input("Ingresar las variables A,B,C D: ").split()
a, b, c, d = datos
a = int(a)
b = int(b)
c = int(c)
d = int(d)
p = a * 1000
s = b*100
t = c*10
c = d*1
den = p+s+t+c
v = round(den, -2)
print("El valor aproximado es: "+str(v))
