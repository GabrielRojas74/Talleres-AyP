"""
entradas
dividendo->int->divid
divisor->int-->divis
salidas
contador->str->cont
"""
divid = int(input("Dividendo: "))
divis = int(input("Divisor: "))
if divid > 0 and divis > 0:
  cont = 0
  res = divid
  while (res >= divis):
    res = res-divis
    cont = cont+1
print(cont)
