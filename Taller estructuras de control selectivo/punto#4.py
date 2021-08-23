"""
entradas
#piezas->int->p
costo_piezas->int->cop
salidas
inversion->str->inv
prestamo->str->pre
credito->str->cr
intereses->str->inter
"""
p=int(input("ingrese el numero de piezas por comprar "))
cop=int(input("ingrese el precio de la pieza "))
t=p*cop
if t>5000000:
 inv=t*0.55
 pre=t*0.30
 cr=t*0.15
else: 
 inv=t*0.70
 pre=0 
 cr=t*0.30
inter=cr*0.20
print("la inversion de la emprsa es de: "+str (inv))
print("El prestamo del banco es por "+str (pre))
print("El credito es de $ "+ str (cr))
print("El credito es de $ " + str(cr))
print("Los intereses del credito son de $ " + str(inter))

