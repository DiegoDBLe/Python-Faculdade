# funcao1.py, definimos uma função chamada multiplica, que multiplica a variável global valor por um fator passado como parâmetro.
# O valor do resultado é atribuído à variável valor novamente (linha 5), que é impresso em seguida (linha 6).
# Ao chamarmos a função multiplica(3) pela primeira vez (linha 8), obtemos a saída “Resultado 60”.
# Como modificamos a própria variável global valor no corpo da função, ao chamarmos novamente a função multiplica(3) (linha 9), obtemos um resultado diferente para a saída: “Resultado 180”.
# Além de não depender apenas dos parâmetros, essa função não retorna valor algum. A função multiplica deste script não é pura.

# EXEMPLO ABAIXO DE FUNÇÃO NÃO PURA:
valor = 20


def multiplica(multiplicador):
    global valor

    valor = valor * multiplicador
    print('FUNÇÃO NÃO PURA - Resultado: ', valor)


multiplica(3)
multiplica(3)
print('-=' * 30)
# EXEMPLO ABAIXO DE UMA FUNÇÃO PURA:
# A função multiplica deste script é um exemplo de função pura, pois depende apenas de seus parâmetros para gerar o resultado,
# e não acessa ou modifica nenhuma variável externa à função e retorna um valor.
valor1 = 10


def multiplica(valor, multiplicador):
    valor = valor * multiplicador
    return valor


print('FUNÇÃO PURA - Resultado: ', multiplica(valor1, 3))
print('FUNÇÃO PURA - Resultado: ', multiplica(valor1, 3))
print('-=' * 30)

# DADOS MUTÁVEIS: ELE MODIFICA A LISTA ORIGINAL ATRAVES DO MÉTODO alterar_lista NA SEGUNDA POSIÇÃO
valores = [10, 20, 30]
valores1 = [40, 50, 60]


def alterar_lista(lista):
    lista[2] = lista[2] + 10
    return lista


print('A nova lista é :', alterar_lista(valores))
print('A nova lista é :', alterar_lista(valores1))
print(valores)
print('-=' * 30)


# DADOS IMUTÁVEIS: CRIADO UMA LISTA DENTRO DO MÉTODO PARA NÃO ALTERAR A LISTA ORIGINAL
def alterar_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista


print('Nova lista', alterar_lista(valores))
print(valores)
