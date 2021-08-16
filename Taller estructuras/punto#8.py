"""
entradas
ladoa-->int-->a
ladob-->int-->b
ladoc-->int-->c
salida
area-->str-->ar
"""
a=int(input("escriba el valor del lado a "))
b=int(input("escriba el valor del lado b "))
c=int(input("escriba el valor del lado c "))
s=(a+b+c)/2
ar=(s*(a-s)*(b-s)*(c-s))**(1/2)
print ("el area del triangulo es " + str (ar))
