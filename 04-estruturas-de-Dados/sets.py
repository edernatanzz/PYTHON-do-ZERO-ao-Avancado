# set (Listas)
#similar a listas
#evita itens duplicados
#não ultiliza index

list1=[10,20,30,40,50]
list2=[10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)   #Union
print(num1 - num2)   #Diference
print(num1 ^ num2)   #Symetric Difference 
print(num1 & num2)   #and 
print(len(num1)) 
print(num1[0]) #perde os index da lista 



