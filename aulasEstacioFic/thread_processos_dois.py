# Neste exemplo, a função que será paralelizada é a funcao_a (linha 7). Ela contém um laço que é executado cem mil vezes e para cada iteração adiciona
# o elemento 1 à lista minha_lista, definida globalmente na linha 5.
# Vamos criar 10 threads (e processos) para executar 10 instâncias dessa função, na qual, esperamos que o número de elementos na lista ao final da execução
# do programa seja de 1 milhão (10 threads X cem mil iterações).
# Para criar essas 10 threads ou processos, temos um laço de 10 iterações (linha 15), em que criamos (linha 16) e iniciamos (linha 18) cada thread ou processo.
# O objetivo da criação de threads ou processos é justamente a computação concorrente ou paralela, o Python não fica “parado” aguardando dela após chamar
# o método start(), ele imediatamente começa a próxima iteração do laço for.

from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []


def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("Termino thread ", indice)


if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))


print('-=' * 30)
print('-=' * 30)
print('-=' * 30)
from threading import Thread, Lock

contador = 0
lock = Lock()
print_lock = Lock()


def funcao_b(indice):

    global contador

    for i in range(1000000):
        lock.acquire()
        contador += 1
        lock.release()
    print_lock.acquire()
    print('Termino thread ', indice)
    print_lock.release()


if __name__ == '__main__':
    tarefas = []

    for indice in range(10):
        tarefa = Thread(target=funcao_b, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
    print("Antes de aguardar o termino!", contador)


    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)

