# # # O que voce quer - Funcional
# numeros = [1, 2, 3, 4]
# print('O total é: ', sum(numeros))
#
#
# # #segundo exemplo:
# print('\nsegundo exemplo: ')
# print('Tudo certo' if True else 'Ops')
#
# lista = ["cachorro", "hamster", ["pato", "galinha", "porco"], "gato"]
# print(lista[3][2])
#
# a, b = 0, 1
# while b < 10:
#     print (b)
#     a, b = b, a+b




from threading import Thread

minha_lista = []


def funcao():
    for i in range(100000):
        minha_lista.append(1)
    for i in range(100000):
        minha_lista.pop()


if __name__=='__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao)
        tarefas.append(tarefa)
        tarefa.start()

    print(len(minha_lista))
    for tarefa in tarefas:
        tarefa.join()
    print(len(minha_lista))


