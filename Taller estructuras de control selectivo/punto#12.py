"""
entradas
valor-->int-->va

"""
cd = int(input("Ingrese cantidad de dinero $"))
bcien = (cd-cd % 100000)/100000
cd=cd % 100000
bcincuen = (cd-cd % 50000)/50000
cd=cd % 50000
bvein = (cd-cd % 20000)/20000
cd=cd % 20000
bdiez = (cd-cd % 10000)/10000
cd=cd % 10000
bcinco = (cd-cd % 5000)/5000
cd=cd % 5000
bd = (cd-cd % 2000)/2000
cd=cd % 2000
bm = (cd-cd % 1000)/1000
cd=cd % 1000
mq = (cd-cd % 500)/500
cd=cd % 500
md = (cd-cd % 200)/200
cd=cd % 200
mc = (cd-cd % 100)/100
cd=cd % 100
mcq = (cd-cd % 50)/50
cd=cd % 50
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
