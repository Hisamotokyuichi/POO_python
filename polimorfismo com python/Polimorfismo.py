
# Inicio do código


# Polimorfismo com Python

# Classe passaros é a classe principal (pai)

class passaros:

    def voar(self):
        print("Voando .........")


# Classe galinha, pinguim e águia são classes filhas

class galinha (passaros):
    def voar(self):
        print("Galinha não voa")


class pinguim (passaros):
    def voar(self):
        print("Pinguim não voa , ele nada !")


class águia (passaros): 
    def voar(self):
        super().voar()


# Função Plano_de_voo , utiliza o polimorfismo para chamar o método voar
    
def Plano_de_voo(objeto):
    objeto.voar()


# instanciação da classe

Plano_de_voo(galinha())
Plano_de_voo(pinguim())
Plano_de_voo(águia())
    

