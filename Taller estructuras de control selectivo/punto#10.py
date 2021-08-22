"""
entradas
salario-->int-->s
categoria-->int-->c
Salidas
aumento-->str-->au
salario nuevo-->str-->sn
"""
s = int(input("Digite el salario $"))
c = int(input("Digite una categoria del 1 al 5: "))
if (c == 1):
  a = s*0.10
if (c == 2):
  a = s*0.15
if (c == 3):
  a = s*0.20
if (c == 4):
 a = s*0.40
 if (c == 5):
  a = s*0.60

sn = s+a

print("su categoria es: "+str(a))
print("Valor del sueldo nuevo $" + str(sn))
