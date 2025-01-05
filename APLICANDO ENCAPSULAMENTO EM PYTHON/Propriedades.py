

# Encapsulamento em Python

# Encapsulamento é o agrupamento de dados e métodos que operam nesses dados em uma única unidade, chamada de classe.

class Foo:
    def __init__(self , x=None):  # quando usado _ antes do nome do atributo, ele é privado
        self._x = x 

# Lembrando que self é uma referência à instância da classe, ou seja, é um objeto que representa a classe.


# @property é um decorador que permite que um método seja chamado como um atributo, sem que seja necessário usar os parênteses.
    @property

    def x(self):
        return self._x or 0
    
# x.setter é um método que permite que o atributo seja modificado.  
    
    @x.setter
    def x(self , value):
         self._x += value
    
# x.deleter é um método que permite que o atributo seja deletado.

    @x.deleter
    def x (self):
         self._x = 0

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Instanciando a classe


foo = Foo(10)  # passando o valor 10 para o atributo x
print(foo.x)   # chamando o método x
del foo.x      # deletando o atributo x
print(foo.x)   # chamando o método x pela 2 vez
foo.x = 20     # passando o valor 20 para o atributo x
print(foo.x)   # chamando o método x pela 3 vez




