

class MeuInterador:
    # Lembrando que __init__ é um construtor !
    def __init__(self , numero: list[int]):  # Numeros : é uma lista de intereiros .

        self.numeros = numero
        self.contador = 0                    # O contador colocamos para que ele saiba da onde começar .

        

    def __iter__(self):
        return self
    
    def __next__(self):
        try: # A função try vai tentar executar o codigo abaixo .

            numero = self.numeros[self.contador] 
            self.contador += 1 # Aqui ele vai adicionar mais um ao contador .
            return numero * 2  # Aqui ele vai multiplicar o numero por 2 .
        except IndexError: # aqui ele vai indentifiar por si só o erro !
            raise StopIteration  # Assim ele vai parar de iterar .


# Agora vamos usar o for para iterar sobre o nosso iterador .

for i in MeuInterador(numero=[10,20,30,40,50]): # Aqui ele vai iterar sobre a lista de numeros .
    print(i)


