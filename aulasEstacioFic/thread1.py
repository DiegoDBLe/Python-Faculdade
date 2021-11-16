import threading
import time

# Exemplo de função sem parametros


def funcao():
    for i in range(3):
        print(i, 'Executando a Thread!')
        time.sleep(0.5)


print('Iniciando o programa!')
threading.Thread(target=funcao).start()  # target sempre recebe o nome da função definida na função. E .start() é para startar a função
print('\nFinalizando...')
