"""
entrada
a-->int-->a
b-->int-->b
c-->int-->c
salida
respuesta-->str-->res
"""
a, b, c, d = map(int, input("escriba los 4 datos ").split()) 
if d==0 :
 res = (a-c)**2
elif d>0 :
    res = ((a-b)**3)/d
print("el resultado es "+str (res))
