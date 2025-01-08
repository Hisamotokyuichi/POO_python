

def Meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2  # O yield é uma ferramenta útil para lidar com grandes conjuntos de dados, pois permite gerar valores sob demanda, sem a necessidade de armazená-los na memória


    for i in Meu_gerador(numeros=[1,2,3,3,4,5]):
        print(i)
