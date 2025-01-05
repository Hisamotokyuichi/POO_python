# Atributos públicos e privados em Python

# Class conta é uma classe que representa uma conta bancária

class conta:
    def __init__(self , nro_agencia , saldo=0):
        # Atributo privado (Ele se torna privado quando é colocado um underline antes do nome do atributo)
        self._saldo = saldo
        self.nro_agencia = nro_agencia


 # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////       

                                # Método público
                                

    # Parametro valor é o valor que será deposit

    def depositar(self , valor):
         self._saldo += valor   # Acessando o atributo privado (no caso o _saldo)
    
        

    # Parametro saque é o valor que será sacado

    def sacar(self , valor):
        self._saldo -= valor


    # Método utilizado para mostrar o saldo

    def mostar_saldo(self):
        return self._saldo



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


conta= conta("0001" , 20  )
conta.depositar(10)

print(conta.mostar_saldo())
print(conta.nro_agencia)






