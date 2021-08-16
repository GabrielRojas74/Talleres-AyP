"""
entrada
hombres-->int-->h
mujeres-->int-->m
salidas
porcentade_de_hombre-->str-->ph
porcentade_de_mujeres-->str-->pm
"""
h=int(input("digite el numero de hombres: "))
m=int(input("digite el numero de mujeres: "))
ct=h+m
ph=((ct-m)*100)/ct
pm=((ct-h)*100)/ct
print("el procentaje de hombres es del:  "+ str(ph),("%"))
print("el procentaje de mujeres es del:  "+ str(pm),("%"))

