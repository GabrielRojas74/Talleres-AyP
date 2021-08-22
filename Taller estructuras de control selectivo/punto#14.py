"""
entradas
lectura_antigua-->float-->lan
lectura_actual-->float-->lac
salida
pago-->str-->p
"""
fac = input("Ingrese los kwh consumidos en el mes pasado y el actual ").split()
(lan, lac) = fac
lan = int(lan)
lac = int(lac)
kv = lac-lan
if(kv >= 0 and kv <= 100):
  p = kv*4600
  print("Total a pagar $"+str(p))
elif(kv >= 101 and kv <= 300):
  p = kv*8000
  print("Total a pagar $"+str(p))
elif(kv >= 301 and kv <= 500):
  p = kv*100000
  print("Total a pagar $"+str(p))
else:
  p = kv*120000
  print("Total a pagar $"+str(p))
