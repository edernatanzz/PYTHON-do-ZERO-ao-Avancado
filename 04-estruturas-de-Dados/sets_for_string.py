#sets (listas )
#evita itens duplicados
# Não ultiliza index

set1= {'a', 'b', 'c'}
set2= {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}


#set4= set1.union(set2)
#set4= set1.difference(set3)
#set4= set1.intersection(set2)
set4=set1.symmetric_difference(set2)

print(set4)