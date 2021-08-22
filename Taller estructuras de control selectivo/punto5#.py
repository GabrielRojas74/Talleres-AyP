"""
entradas:
importe_global--->float--->ig
sueldo_base--->float--->sb
venta1--->float--->vu
venta2--->float--->vd
venta3--->float--->vt
Salidas:
sueldo1--->str--->su
sueldo2--->str--->sd
sueldo3--->str--->st
"""
ig = float(input("ingrese el valor del importe global: "))
sb = float(input("ingrese el valor del sueldo basico: "))
vu = float(input(" valor de ventas del departamento 1: "))
vd = float(input(" valor de ventas del departamento 2: "))
vt = float(input(" valor de ventas del departamento 3: "))
p1 = ((vu*100)/ig)
p2 = ((vd*100)/ig)
p3 = ((vt*100)/ig)
st = (sb+(sb*0.2))
if(p1 > 33):
  print("Salario vendeor 1: "+str(st))
else:
  print("Sueldo vendeor 1: "+str(sb))
if(p2 > 33):
  print("Salario vendeor 2: "+str(st))
else:
  print("Sueldo vendeor 2: "+str(sb))
if(p3 > 33):
  print("Salario vendeor 3: "+str(st))
else:
  print("Sueldo vendeor 3: "+str(sb))
