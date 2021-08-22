"""
entrada
nombre->int->n
monto_compra-->int-->mc
salidas
total_descuento->str->td
"""
n = str(input("nombre del cliente: "))
mc = int(input("ingrese el valor de la compra $"))
if (mc < 50000):
    print(n)
    print("No hay descuento")
    print("Monto a pagar: " + str(mc),"$")
elif(mc > 50000 and mc <= 100000):
  td = mc*0.05
  mcb = mc-td
  print("Nombre del cliente: "+str(n))
  print("Su momto de compra es: " + str(mc))
  print("Su descuento por la compra es de: " (td),"$")
  print("Su valor a pagar es de: " (mcb), "$")
elif (mc >= 100000 and mc < 700000):
    td = mc*0.11
    mcb = mc-td
    print("Nombre del cliente: "+str(n))
    print("Su momto de compra es: " + str(mc))
    print("Su descuento por la compra es de: "+str(td)," $")
    print("Su valor a pagar es de: "+str(mcb), " $")
elif (mc >= 700000 and mc < 1500000):
    td = mc*0.18
    mcb = mc-td
    print("Nombre del cliente: "+str(n))
    print("Su momto de compra es: " + str(mc))
    print("Su descuento por la compra es de: " +str(td), " $")
    print("Su valor a pagar es de: "+str(mcb), " $")
elif (mc >= 1500000):
    td = mc*0.25
    mcb = mc-td
    print("Nombre del cliente: "+str(n))
    print("Su momto de compra es: " + str(mc))
    print("Su descuento por la compra es de: " +str(td), " $")
    print("Su valor a pagar es de: "+str(mcb), " $")

