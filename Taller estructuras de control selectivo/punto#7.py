"""
entradas:
km_recorridos-->float-->kr
Salidas:
Tarifa-->float-->valor
"""
kr = float(input("escriba la distancia recorrida en Km: "))
if(kr <= 300 and kr > 0):
  valor = 50000
  print("el valor a pagar es $"+str(valor))
elif(kr > 300 and kr <= 1000):
  valor = (70000+((kr-300)*30000))
  print("el valor a pagar es $"+str(valor))
if(kr > 1000):
  valor = (150000+((kr-1000)*9000))
  print("el valor a pagar es $"+str(valor))
