# A função map é utilizada para aplicar uma determinada função em cada elemento de um iterável (lista, tupla, dicionários etc.),
# retornando um novo iterável com os valores modificados.
# A função map é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro. A sua sintaxe é a seguinte:
# map(função, iterável1, iterável2...)

#No exemplo do Codigo 7, a seguir, vamos criar três scripts. Todos executam a mesma operação.
# Recebem uma lista e triplicam cada item, gerando uma nova lista com os valores triplicados.

lista = [1, 2, 3, 4, 5]
print('lista: ', lista)


def triplica_itens(itens):

    lista_aux = []

    for item in itens:

      lista_aux.append(item * 3)

    return lista_aux


nova_lista = triplica_itens(lista)
print('Triplicando os valores da lista: ', nova_lista)

# Utilizando a função map no lugar do for.

listaA = [6, 7, 8, 9, 10]
print('listaA', listaA)


def triplica(item):

    return item * 3


nova_lista_A = map(triplica, listaA)
print('Tripicando usando map', list(nova_lista_A))


# Agora usando map e lambda para tripicar os valores da lista:
listaB = [11, 12, 13, 14, 15]
print('listaB', listaB)


nova_lista_B = map(lambda item: item * 3, listaB)
print('Triplicando a listaB usando map e lambda ', list(nova_lista_B))
