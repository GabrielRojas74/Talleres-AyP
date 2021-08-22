"""
entradas
edad-->int-->e
hemoglobina-->int-->hemo
salidas
resultado-->str--r
"""
e = int(input("ingrese su edad en meses "))
hemo = float(input("Ingrese su nivel de hemoglobina en % "))
if(e >= 0 and e <= 1):
  if(hemo >= 12 and hemo <= 26):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(e > 1 and e <= 6):
  if(hemo >= 10 and hemo <= 18):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(e > 6 and e <= 12):
  if(hemo >= 11 and hemo <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(e > 12 and e <= 60):
  if(hemo >= 11.5 and hemo <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(e > 60 and e <= 120):
  if(hemo >= 12.6 and hemo <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(e > 120 and e <= 180):
  if(hemo >= 13 and hemo <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
