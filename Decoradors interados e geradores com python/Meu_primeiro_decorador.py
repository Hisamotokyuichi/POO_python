# Inicio do Código 



def Meu_decorador(funcao):

    def envelope():
        print("Antes da execução da função")
        funcao()
        print("Depois da funcao")

    return envelope
@Meu_decorador
def ola_mundo():
    print("Olá mundo!")

#ola_mundo = Meu_decorador(ola_mundo)  ////// # Para não precisar ficar passando o meu decorador vamos usar o açucar sintatico !
ola_mundo()


# Fim do Código