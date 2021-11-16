palavra = input('Entre com uma palavra: ')
while palavra != 'sair':
    palavra = input('Digite "sair" para encerrar o laço: ').strip()
print('Você digitou sair e agora está fora do laço. ')

soma_pares = 0
cont_pares = 0

for numero in range(1, 11, 1):
    if numero % 2 == 0:
        soma_pares += numero
        cont_pares += 1
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')

print(f'A soma dos pares foi: {soma_pares} e a qauntidade de pares foi de : {cont_pares}')
print(f'A média da soma dos pares é de: {soma_pares / cont_pares}')

# AS INSTRUÇÕES AUXILIARES BREAK, CONTINUE E PASS
# A instrução break:
# A instrução break funciona da mesma maneira em C e em Python. Ela interrompe as repetições dos laços for e while.
# Quando a execução do programa chega a uma instrução break, a repetição é encerrada e o fluxo do programa segue a partir da primeira instrução seguinte ao laço.
# Para exemplificar o uso da instrução break, vamos voltar ao primeiro exemplo do laço while, utilizando o laço infinito.
# O laço será encerrado quando o usuário inserir a palavra ‘sair’.

# A instrução continue
# A instrução continue também funciona da mesma maneira em C e em Python. Ela atua sobre as repetições dos laços for e while, como a instrução break, mas não interrompe todas as repetições do laço.
# A instrução continue interrompe apenas a iteração corrente, fazendo com que o laço passe para a próxima iteração.
# O exemplo a seguir imprime todos os números inteiros de 1 até 10, pulando apenas o 5.

for num in range(1, 11):
    if num == 5 or num == 7:
        continue
    else:
        print(num)
print('Laço encerrado!')

# A INSTRUÇÃO PASS
# A instrução pass atua sobre a estrutura if, permitindo que ela seja escrita sem outras instruções a serem executadas caso a condição seja verdadeira.
# Assim, podemos concentrar as instruções no caso em que a condição seja falsa. Suponha que queiramos imprimir somente os números ímpares entre 1 e 10.

for numero1 in range(1, 11):

    if numero1 % 2 == 0:
        pass
    else:
        print(numero1)
print('ACABOU!')
s = 0
for i in range(5):
    s += 3* i
print(f'Soma= {s} ')

# FUNÇÃO, DEF
def func1(x):
    return x + 1

escolha = input('Escolha uma da opções de função: 1 ou 2: ')
if escolha == 1:
    def func1(x):
        return x + 1
else:
    def func2(x):
        return x + 2
s = func1(10)
print(f'Função= {s}')

# PARAMETROS
def taximetro(distancia, multiplicador = 1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    print(f'Largada = {largada} + distancia = {distancia} + km_rodado = {km_rodado} * multiplicador = {multiplicador}')
    return valor
pagamento = taximetro(3.5)
print(f'PAGAMENTO R${pagamento}')
print(taximetro(2.5))

# FUNÇÃO X PROCEDIMENTO
def funcAb(y):
    y = 10
    print(f'Função funcAb - x = {y}')
def funcBc(x):
    x = 20
    print(f'Função funcBc - x = {x}')

x = 0
y = 0
funcAb(y)
funcBc(x)
print(f'Programa principal - x {y} e {x}')

# RECURSIVIDADE
def regressividade(x):
    if x < 0:
        print('ACABOU!')
    else:
        print(x)
        regressividade(x - 1)

