al = 0
ga = 0
di = 0
n = 0
while n != 4:
    n = int(input())
    if n == 1:
        al = al+1
    if n == 2:
        ga = ga+1
    if n == 3:
        di = di+1
print("MUITO OBRIGADO")
print("Alcool: " + str(al))
print("Gasolina: " + str(ga))
print("Diesel: " + str(di))
