# Inicio Do Codigo


# Atributos de class ou de instancias abstratas


class Estudante :
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula 


# __str__ é um metodo especial que retorna uma representação de string de um objeto

    def __str__(self):
        return f"{self.nome} da escola {self.escola} com a matricula {self.matricula}"
    

# Metodo para mostrar os dados do aluno
def mostrar_Dados_do_aluno(*objs):
    for obj in objs:
        print(obj)
    


# Instanciando um objeto da classe Estudante


aluno_1 = Estudante(" Isaque " , 1 , )
aluno_2 = Estudante(" Kyuchi " , 2 , )

# Mostrando os dados do aluno

mostrar_Dados_do_aluno(aluno_1, aluno_2)

# mudando o atributo de class escola 

Estudante.escola = "Dio Python"  # Aqui vemos que mudamos o atributo de class escola para "Dio Python"

# Mudando o atributo de instancia escola

aluno_1.escola = "Dio Java"  # Aqui vemos que mudamos o atributo de instancia escola para "Dio Java" , que afetara somente o aluno_1 e não o aluno_2 . 

# Mostrando os dados do aluno

mostrar_Dados_do_aluno(aluno_1, aluno_2)

# Fim Do Codigo , obrigado por ler ate aqui.

