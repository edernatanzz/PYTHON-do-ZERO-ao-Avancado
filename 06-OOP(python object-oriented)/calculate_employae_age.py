from datetime import datetime 

#criar classe 
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome= sobrenome
        self.ano_nascimento= ano_nascimento
    def nome_completo(self):
        return(self.nome + ' ' + self.sobrenome)


    def idade(self):
        ano_atual = datetime.now().year
        #return(2023 - self.ano_nascimento )
        return(ano_atual - self.ano_nascimento)
        



#criar o objeto + parametros 
usuario1 = Funcionarios('Eder ', ' nattan ' , 2001)
usuario2 = Funcionarios('edi', 'costa', 2008)


print(Funcionarios.idade(usuario1))
print(Funcionarios.idade(usuario2))
