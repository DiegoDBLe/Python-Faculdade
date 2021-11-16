# É utilizada para filtrar elementos de um iterável (lista, tupla, dicionários etc.). O filtro é realizado utilizando uma função,
# que deve ser capaz de retornar true ou false para cada elemento do iterável.
# Todo elemento que for avaliado como true será incluído em um novo iterável retornado pela função filter,
#  que é pura e de alta ordem, pois depende apenas dos parâmetros e recebe uma função como parâmetro. A sua sintaxe é a seguinte:
# filter(função, iterável)


#Definimos uma função chamada ímpares, que recebe um iterável como parâmetro, cria uma lista auxiliar para garantir imutabilidade, percorre os itens do
# iterável passados como parâmetros, adiciona os itens ímpares à lista auxiliar e retorna a lista auxiliar.Essa função é chamada com o argumento lista
# e o resultado é impresso .
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista:{lista}')


def impares(interable):
    lista_auxiliar = []
    for item in interable:
        if item % 2 != 0:
            lista_auxiliar.append(item)
    return lista_auxiliar


nova_lista = impares(lista)
print(f'função com for, somente numero impares da lista: {nova_lista}')


# Definimos a função ímpar, que retorna true se o item passado como parâmetro é ímpar ou false caso contrário. Utilizamos essa função, assim como a variável
# lista, como argumentos para a função filter.A filter vai aplicar, internamente, a função passada como parâmetro em cada item da lista, retornando um novo
# iterável (que pode ser convertido em listas, tuplas etc.). O resultado da função filter é armazenado na variável nova_lista, para então ser impresso.
# A função filter garante a imutabilidade dos iteráveis passados como argumento. Como a função filter retorna um iterável, utilizamos o construtor
# list(iterável) para imprimir o resultado.
lista_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista: {lista_A}')


def impar(item):
    return item % 2 != 0


lista_nova = filter(impar, lista)
print(f'a função com filter, somente números impares da lista: {list(lista_nova)}')

#Substituímos a função ímpar pela função lambda (lambda item: item%2 != 0) que foi utilizada como argumento para a função filter.
# Esta vai aplicar a função lambda em cada item da lista, retornando um novo iterável que foi impresso posteriormente.
lista_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista: {lista_B}')

lista_nova_B = filter(lambda item: item % 2 != 0, lista_B)
print(f'Lista usando filter e lambda. Mostrando somente os números impares: {list(lista_nova_B)}')
