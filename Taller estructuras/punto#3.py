"""
entradas
suendo_base-->float-->sb
venta1-->float-->vu 
venta2-->float-->vd
venta3-->float-->vt
salidas
comision-->str-->com
sueldo_total-->str-->st
"""
sb = float(input("ingrese su sueldo base"))
vu = float(input("ingrese el valor de la venta #1 "))
vd = float(input("ingrese el valor de la venta #2 "))
vt = float(input("ingrese el valor de la venta #3 "))
com=(vu+vd+vt)*0.10
st=com+sb
print("sus ganancias por comision son: "+ str (com) )
print("el total de su sueldo es: "+ str (st)) 

