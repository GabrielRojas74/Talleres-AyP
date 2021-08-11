"""
entrada
total_compra-->float-->tc
Salida
precio_total-->float-->pt
"""
tc= float(input("escriba el total de su compra"))
vd=(tc*0.15)
pt=tc-vd
print("el valor total de su compra es: ",str(pt))
