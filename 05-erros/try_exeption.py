# erros
#exelemtes para testes
#não realiza o 'stop' no programa
#mensagens customizadas quando encontra um erro 



try: 
  letras = [ 'a', 'b' , 'c' ]
  print(letras[3])
except IndexError:
  print('index inexistente !')
