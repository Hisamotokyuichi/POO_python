
# Implementação de encapsulamento em Python
  
          # Inicio do código 

#  class pessoas é a classe principal (pai)


class pessoas:
    def __init__(self , nome , ano_nacimento):
        self._nome = nome 
        self._ano_nacimento = ano_nacimento


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# O metodo é uma função que pertence a uma classe, e é chamado de método de instância, pois é chamado por uma instância da classe.


    @property  # @property é um decorador que permite que um método seja chamado como um atributo, sem que seja necessário usar os parênteses.
    def nome(self):         # self é uma referência à instância da classe, ou seja, é um objeto que representa a classe.
        return self._nome   # retorna o nome
        

    @property
    def idade(self):
        _ano_atual = 2025  # ano atual
        return _ano_atual - self._ano_nacimento  # retorna a idade
    

    # instanciação da classe

pessoa = pessoas("isaque", 1999) # passando o nome e o ano de nascimento
print(f"Nome: {pessoa.nome}\tIdade: {pessoa.idade}")  

# \t é um caractere de escape que representa um tabulação, ou seja, ele pula 8 espaços na tela.

# Fim do código