
# Definindo a class Poo_com_Python.py para 

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
# Self é uma referência a instância da classe, ou seja, o objeto que está sendo criado.
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano 
        self.valor =valor
        

# metodos são funções que pertencem a uma classe

    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("parando a bicicleta ....")
        print("bicicleta parada")

    def correr (self):
        print("zummmmmm........")
        print("bicicleta correndo")


    def  trocar_de_marcha(self):
        print("marcha trocada")

        # Um exemplo de método que recebe um parâmetro e faz uma comparação com um atributo da classe.

        #def _trocando_marcha():
           # if nro_marcha > self.marcha:
             #  print("marcha trocada ")
            #else:
              #  print("Não foi possivel ....")
            
        
    #/////////////////////////////////////////////////////////////////////////////


    # Método especial para representar a classe
    # O método __str__ é um método especial que retorna uma representação da classe em forma de string.
    #__dict__ é um atributo especial que retorna um dicionário contendo os atributos da classe.

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join ( [ f" {chave}={valor}" for chave ,valor in self.__dict__.items()])}"




# Instanciando a classe Bicicleta

b1 = Bicicleta("verde","Caloi",2020,500.00)

b1.buzinar()
b1.parar()
b1.correr()

#Chamando os atributos da classe Bicicleta

print(b1)