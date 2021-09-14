"""8.Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista"""
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
tipo-->type-->type
"""
frutas = open('frutas.txt', 'r')
lista_frutas = []
for i in frutas:
  lista_frutas.append(i)
def eliminar_un_caracter(lista, elemento):
  auxilar = []
  for i in lista:
    a = i.replace(elemento, "")
    auxilar.append(a)
  return auxilar
def informacion_lista(lista):
  aux = []
  for i in lista:
    print(len(lista))
    return aux
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, "\n")
  nueva_fin = informacion_lista(nueva)
  print(type(nueva_fin))
