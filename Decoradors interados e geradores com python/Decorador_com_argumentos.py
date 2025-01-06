# Inicio do Código 



def Meu_decorador(funcao):

    def envelope(*args ,**kwargs): # O *args e **kwargs são utilisados para passar um número variável de argumentos para uma função. Isso permite que a função aceite qualquer quantidade de argumentos posicionais e/ou nomeados, sem precisar especificar explicitamente quantos argumentos ela deve receber.
        print("Antes da execução da função")
        funcao(*args ,**kwargs)
        print("Depois da funcao")



    return envelope



@Meu_decorador
def ola_mundo(nome , qualquer_argumento_a_mais):
    print(f"Olá mundo! {nome}")

ola_mundo("isaque", 123)   # Veja que 123 é um argumento a mais que a função ola_mundo() não espera, mas o decorador @Meu_decorador permite que isso aconteça sem gerar um erro.


# Fim do Código     