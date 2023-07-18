#armazenar mais de uma informação em variaveis 
#manter a sequencia dos dados em uma variavel 
produtos=['arroz','feijao', 'laraja', 'banana',5,6,7,8]
#            0        1         2         3

item1,item2, *outros,item8 =produtos;

print(item1)
print(item2)
print(outros);
