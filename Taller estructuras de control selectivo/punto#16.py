"""
entradas
valorA-->float-->A
valorB-->float-->B
valorC-->float-->C
salidas
valor_x1-->str-->xu
valor_x2-->str-->xd
"""
A = float(input("Ingrese el valor de A "))
B = float(input("Ingrese el valor de B "))
C = float(input("Ingrese el valor de C "))
D = B**2-4*A*C
if(D == 0):
  xu = xd = -B/(2*A)
  print("El valor de xu es "+str(xu)+" y el valor de x2 es "+str(xd))
elif(D > 0):
  xu = (-B+(B**2-4*A*C)**0.5)/(2*A)
  xd = (-B-(B**2-4*A*C)**0.5)/(2*A)
  print("El valor de x1 es "+str(xu)+" y el valor de x2 es "+str(xd))
else:
  print("no tiene solución en los Reales.")
