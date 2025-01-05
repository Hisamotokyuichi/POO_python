
# Herança simples é quando uma classe herda de apenas uma classe pai.

# Exemplo de herança simples
class veiculo :
    def __init__(self , cor ,placa , numero_de_rodas):

        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

# método para ligar o motor
    def ligar_motor (self):
        print('motor ligado')
    
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join ( [ f" {chave}={valor}" for chave ,valor in self.__dict__.items()])}"
        
#class filhas


class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_de_rodas , carregado = False ):
        self.carregado = carregado 
        super().__init__(cor, placa, numero_de_rodas)

# self é uma referência a instância da classe
    def esta_carregado(self):
        # se o caminhão estiver carregado imprime sim, se não imprime não
        print(f"{"sim bem carregado" if self.carregado else "não esta carregado"}")
        


#instanciando objetos

moto = motocicleta( "preta " , " nnnn-25" , 2 )
moto.ligar_motor()

#instanciando objetos

car = carro("vermelho" , " nnnn-25 ", 4 )   
car.ligar_motor()

#instanciando objetos

caminhao = caminhao("branco" , "nnnn-25" , 8 , True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)