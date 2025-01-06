# Inicio do Código 



def Meu_decorador(funcao):

    def envelope(*args ,**kwargs): 
        print("Antes da execução da função")
        resultado = funcao(*args ,**kwargs)   
        print("Depois da funcao")
        return resultado 
    # Oque fizemos ? colocamos o resultado para retornar dentro da Função do envelope , assim podendo fazer um código mais seguro  ! 



    return envelope



@Meu_decorador
def ola_mundo(nome , qualquer_argumento_a_mais):
    print(f"Olá mundo! {nome}")
    return nome.upper()  # lembrando O comando upper() é utilizado para o valor sair tudo em MAIUSCULO!

resultado = ola_mundo("isaque", 123)  
print(resultado)

# Fim do Código  