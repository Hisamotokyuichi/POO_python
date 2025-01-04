

# construtores e descostrutores

# Construtores são métodos especiais que são chamados automaticamente quando um objeto é criado.
# O construtor é um método especial chamado __init__.

# A class cachorro tem um construtor que recebe 4 parâmetros: nome, cor, idade e acordado.

class cachorro :
    def __init__(self,nome,cor,idade,acordado=True):
        print("Construindo um objeto da classe cachorro")
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.acordado = acordado


    # __del__ é um método especial que é chamado automaticamente quando um objeto é destruído.

    def __del__(self):
        print("Destruindo um objeto da classe cachorro")


    # Método especial para representar a classe

    def latir (self):
        print ("au,au,au")

def criar_cachorro():
    c = cachorro("aladim","preto",50, False)
    print(c.cor)

    
# Instanciando a classe cachorro   
 
c = cachorro ("Rex","preto",2)
c.latir()

del c
criar_cachorro()


