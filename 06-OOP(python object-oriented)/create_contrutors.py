
#criar classe 
class Funcionarios :
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento



#criar o objeto + parametros 
usuario1 = Funcionarios('Eder' , 'Natan' ,'03/09/2001')
usuario2 = Funcionarios('edi', 'costa' , '31/01/2008')



#print
print(usuario1.nome)
print(usuario2.nome)