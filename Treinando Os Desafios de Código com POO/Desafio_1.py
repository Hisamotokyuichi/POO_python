# TODO: Crie uma classe e método para realizar a soma:


class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def soma(self , num1 , num2):
        return num1 + num2
    
  
  
    
    


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Criando uma instância da calculadora
calc = Calculadora(num1,num2)

resultado = calc.soma(num1, num2)
print(resultado)


#fim do código , obrigado pela atenção!