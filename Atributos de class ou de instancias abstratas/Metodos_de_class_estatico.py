
#Inicio do Codigo


# Metodos de class estatico

class Pessoa :
    def __init__(self , nome=None , idade=None ):
        self.nome = nome
        self.idade = idade


# class method è um metodo que recebe a class como primeiro argumento
    @classmethod
    def Cria_A_data_nacimento(cls , ano , mes , dia , nome ):
        idade = 2025 - ano
        return cls(nome , idade)
    
 # static method è um metodo que não recebe a class como primeiro argumento    
    @staticmethod
    def Maior_de_idade(idade):
        return idade >= 18
    

# Instanciando um objeto da classe Pessoa

pessoa_1 = Pessoa.Cria_A_data_nacimento(1999 , 10 , 2 , "Isaque Hisamoto")

# Mostrando os dados da pessoa
print(pessoa_1.nome, pessoa_1.idade)

# Verificando se a pessoa è maior de idade
print(Pessoa.Maior_de_idade(pessoa_1.idade))


# Fim Do Codigo , obrigado por ler ate aqui.
    


