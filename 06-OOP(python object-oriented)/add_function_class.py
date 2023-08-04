
#criar classe 
class Funcionarios :
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome




#criar o objeto + parametros 
usuario1 = Funcionarios('Eder' , 'Natan' ,'03/09/2001')
usuario2 = Funcionarios('edi', 'costa' , '31/01/2008')



#print
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
