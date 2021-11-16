import threading
import time

# Exemplo de função com passagem de parametros:


def funcao(mensagem):
    for i in range(3):
        print('\n', i, mensagem)
        time.sleep(0.5)


print('Inicializando...')
x = threading.Thread(target=funcao, args=('Executando!',)) # args corresponde ao parametro da função. Nesse exemplo a mensagem que quero imprimir
x.start() # como coloquei minha thread em uma variavel, aqui estou startando ela.
print('\nFinalizando o Programa!')
