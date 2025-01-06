

class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def __str__(self):
      return  f"Nome: {self.nome},\t Idade: {self.idade}"
      
def mostrar_dados_da_pessoa(*objs):
  for obj in objs :
    print(obj)
    
    

# Entrada do usuário
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua Idade:"))

# TODO: Crie uma instância da pessoa:
pessoa = Pessoa(nome,idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:

mostrar_dados_da_pessoa(pessoa)


#fim do codigo # 
