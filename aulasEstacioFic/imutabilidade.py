# Imutabilidade: Onde você não altera o valor da variavel

def sum(numeros):
    if not numeros:
        return 0
    primeiro = numeros[0] #pega o primeiro numero na posição zero
    resto = numeros[1:] #pega o número a partir da posição 1 até o final da lista
    return primeiro + sum(resto) # soma o primeiro numero na posição zero + o resto que é o numero na posição um até o final da lista


print(sum([2, 4, 6, 8, 10]))


#segundo exemplo:
print('\nsegundo exemplo: ')
lista = ['ferrari']
nova_lista = lista + ['porcher'] # ou seja não aletrou o valor da lista
print(nova_lista)
print(lista)
