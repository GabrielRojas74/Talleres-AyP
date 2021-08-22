
"""
entradas:
valor_p-->int-->P
valor_q-->int-->Q
Salidas:
Expresion-->str-->ex
"""
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))
t = (P**3)+(Q**4)-(2*P**2)
if(t < 680):
    print(str(P),"y"+str(Q),"no satisfacen la expresión")
elif(t > 680):
    print(str(P),"y"+str(Q),"satisfacen la expresión")
