# Inicio do codigo

# Importando a biblioteca abc

from abc import ABC, abstractmethod , abstractproperty

class controle(ABC):


    @abstractmethod   # Decorator que indica que o metodo é abstrato
    def ligado(self):
        pass

    @abstractmethod
    def desligado(self):
        pass

    @property
    @abstractproperty  # Decorator que indica que o metodo é abstrato
    def marca(self):
        pass
    
# Criando uma classe TV que herda da classe controle

class TV(controle):  # Herança

    
    def ligado(self):
        print("Ligando a TV")
        print("Ligada.....")

    
    def desligado(self):
        print("Desligando a TV")
        print("Desligada.....")

    @property          # Decorator que indica que o metodo
    def marca(self):
        return "Samsung"
    

class Ar_condicionado(controle):

    def ligado(self):
        print("Ligando o Ar condicionado")
        print("Ligado.....")

    def desligado(self):
        print("Desligando o Ar condicionado")
        print("Desligado.....")

    @property
    def marca(self):
        return "LG"
    
# Instanciando as classes

controle = TV()
controle.ligado()
controle.desligado()
print(controle.marca)

# Instanciando as classes

controle = Ar_condicionado()
controle.ligado()
controle.desligado()
print(controle.marca)





# Fim do codigo , obrigado pela atenção


    
