import threading
import time

# Exemplo de sincronização de threads com passagem de parametros:
# declaramos uma lista e declaramos duas funções, contador 1 e contador 2 ambos recebem parametros, faz um for ate o numero passado em parametro.
# printa o indice, e adiciona dentro da lista, time sleep, depois cria uma variavel para colocar a primeira thread e starta ela.
# depois cria outra variavel que recebe a thread e starta ela e depois print da lista
lista = []


def contador1(n):
    for i in range(1, n+1):
        print(i, 'Contador 1')
        lista.append(i)
        time.sleep(0.5)


def contador2(n):
    for i in range(6, n+1):
        print(i, 'Contador 2')
        lista.append(i)
        time.sleep(0.6)


x = threading.Thread(target=contador1, args=(5,))
# Dando o start ele sai printando a função contador 1 e contador 2 e printando a lista de forma desorganizada
x.start()

# Esse join() abaixo quer dizer que execute a thread da variavel x primeiro e depois voce executa a thread da variavel y e quando terminar a execução das duas
# execute a função print. join (junte)
x.join()

y = threading.Thread(target=contador2, args=(10,))
y.start()

# Abaixo estou usando o método join() nas duas vaiaveis, ou seja depois de executar todas as funções o programa vai executar o print de forma organizada.
#x.join()
y.join()

print(lista)
