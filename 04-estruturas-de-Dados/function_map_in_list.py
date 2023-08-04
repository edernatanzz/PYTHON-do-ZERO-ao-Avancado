# Map function
#muito ultilizado com listas
#aplicar uma função a um iterable, por item. (list, tuple,dic.etc.0

lista1= [1, 2, 3, 4 ]

def multi(x):
    return x * 2 


print(multi(2))


lista2= map(multi, lista1 )
print(lista2)

