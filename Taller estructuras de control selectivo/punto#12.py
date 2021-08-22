"""
entradas
valor-->int-->va

"""
a = int(input("Ingrese cantidad de dinero $"))
b = a
bcien = (b-b % 100000)/100000
b = b % 100000
bcincuen = (b-b % 50000)/50000
b = b % 50000
bvein = (b-b % 20000)/20000
b = b % 20000
bdiez = (b-b % 10000)/10000
b = b % 10000
bcinco = (b-b % 5000)/5000
b = b % 5000
bd = (b-b % 2000)/2000
b = b % 2000
bm = (b-b % 1000)/1000
b = b % 1000
mq = (b-b % 500)/500
b = b % 500
md = (b-b % 200)/200
b = b % 200
mc = (b-b % 100)/100
b = b % 100
mcq = (b-b % 50)/50
b = b % 50
if bcien>0:
    print("La Cantidad de billetes de 100000 es de: "+str(bcien))
if bcincuen > 0:
    print("La Cantidad de billetes de 50000 es de: "+str(bcincuen))
if bvein > 0:
    print("La Cantidad de billetes de 20000 es de: "+str(bvein))
if bdiez > 0:
    print("La Cantidad de billetes de 10000 es de: "+str(bdiez))
if bcinco > 0:
    print("La Cantidad de billetes de 5000 es de: "+str(bcinco))
if bd > 0:
    print("La Cantidad de billetes de 2000 es de: "+str(bd))
if bm > 0:
    print("La Cantidad de billetes de 1000 es de: "+str(bm))
if mq > 0:
    print("La Cantidad de monedas de 500 es de: "+str(mq))
if md > 0:
    print("La Cantidad de monedas de 200 es de: "+str(md))
if mc > 0:
    print("La Cantidad de monedas de 100 es de: "+str(mc))
if mcq > 0:
    print("La Cantidad de monedas de 50 es de: "+str(mcq))
