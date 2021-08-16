"""
entradad
nota_pacial1-->float-->nu
nota_pacial2-->float-->nd
nota_pacial3-->float-->nt
examen_final-->float-->ef
trabajo_final-->float-->tf
salidas
nota_final-->str-->nf
"""
nu = float (input("dijite su nota #1  "))
nd = float (input("dijite su nota #2  "))
nt = float (input("dijite su nota #3  "))
ef = float(input("escriba la nota de su examen final  "))
tf = float(input("escriba la nota de su trabajo final  "))
cc=(nu+nd+nt)/3
nt=(cc*0.55)+(ef*0.3)+(tf*0.15)
print("su nota final es: "+str (nt))


