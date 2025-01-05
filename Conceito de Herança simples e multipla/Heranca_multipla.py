


#Herança multipla é quando uma classe filha herda de mais de uma classe pai.

class animais():
    def __init__(self , nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join ( [ f" {chave}={valor}" for chave ,valor in self.__dict__.items()])}"

#classe filha

# Argumentos de inicialização da classe mamiferos e ave são diferentes, por isso é necessário passar os argumentos de inicialização da classe pai para as classes filhas.

# SUper() é usado para chamar o método da classe pai.

class mamiferos(animais): 

    def __init__(self,  cor_pelo , **KW):
        self.cor_pelo = cor_pelo
        super().__init__(**KW)  # **kw é usado para passar os argumentos de inicialização da classe pai para a classe filha.

#classe filha

class ave(animais):
    def __init__(self,  cor_de_bico , **KW):
        self.cor_de_pico = cor_de_bico
        super().__init__(**KW)

#classe filha

class gato(mamiferos):
    pass

# MIXIN é uma classe que não é uma classe pai, mas que pode ser usada para adicionar funcionalidades a outras classes.
class falarmixin:
    def falar(self):
        return "olá estou falando"

#classe filha

class onitorrinco(mamiferos , ave , falarmixin):
    pass

        

gato = gato(nro_patas=2 ,cor_pelo="preto")
#print(gato)  

onitorrinco = onitorrinco(nro_patas= 4 ,cor_pelo= "marrom" ,cor_de_bico= "laranja")
#print(onitorrinco)

print(onitorrinco.falar())