"""
entrada
inversion-->int-->inv
tasa-->int-->t
salida
dinero_final-->str-->fd
"""
entradas =input("ingrese el valor de la inversion y de la tasa de interes ").split()
(inv, t)=entradas
inv=int(inv)
t=int(t)
inter=inv*t
if inter>100000:
    print("los intereses generados son de "+str (inter), " asi que exeden los $100000")
else:
    print("los intereses generados son de " +str(inter), " asi que no exeden los $100000")

