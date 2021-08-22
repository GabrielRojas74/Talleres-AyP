"""
entradas
dia-->int-->d
mes-->int-->m
Salidas
singno-->int->s
"""
d = int(input('Digite el numero de dia: '))
m = int(input("Digite el numero de mes: "))

if (d >= 21 and m == 3) or (d <= 20 and m == 4):
    print('Aries')
if (d >= 24 and m == 9) or (d <= 23 and m == 10):
    print('Libra')
if (d >= 21 and m == 4) or (d <= 21 and m == 5):
    print('Tauro')
if (d >= 24 and m == 10) or (d <= 22 and m == 11):
    print('Escorpio')
if (d >= 22 and m == 5) or (d <= 21 and m == 6):
    print('Geminis')
if (d >= 23 and m == 11) or (d <= 21 and m == 12):
    print('Sagitario')
if (d >= 21 and m == 6) or (d <= 23 and m == 7):
    print('Cancer')
if (d >= 22 and m == 12) or (d <= 20 and m == 1):
    print('Capricornio')
if (d >= 24 and m == 7) or (d <= 23 and m == 8):
    print('Leo')
if (d >= 21 and m == 1) or (d <= 19 and m == 2):
    print('Acuario')
if (d >= 24 and m == 8) or (d <= 23 and m == 9):
    print('Virgo')
if (d >= 20 and m == 2) or (d <= 20 and m == 3):
    print('Piscis')
