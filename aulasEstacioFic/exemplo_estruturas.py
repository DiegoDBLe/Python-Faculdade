# numero = eval(input('Entre com um número inteiro: '))
#
# if numero % 2 == 0:
#     print('Número informado é Par.')
# else:
#     print('Número informado é Impar.')
#
# print('==' * 30)
# print('')
# for c in range(1, 11):
#     if c % 2 == 0:
#         print(f'{c} é par')
#     else:
#         print(f'{c} é Impar.')
# print('==' * 30)
# print('')
#
# soma_pares = tot_pares = 0
# for c in range(1, numero + 1):
#     if c % 2 == 0:
#         soma_pares += c
#         tot_pares += 1
#     else:
#         print(f'{c} é Impar.')
# print(
#     f'Somando os pares = {soma_pares} \nTotal de pares entre 1 e {numero} é : = {tot_pares} \nMédia dos pares é: = {soma_pares / tot_pares}')
# print('==' * 30)
# print('')
#
# soma = 0
# for i in range(5):
#     soma += 3 * i
# print(soma)
#
# def func1(x):
#     return x + 1
# def func2(x):
#     return x + 2
# escolha = input("Escolha uma opção de função: 1 ou 2")
# if escolha == 1:
#     def func1(x):
#         return x + 1
# else:
#     def func2(x):
#         return x + 2
# s = func1(10)
# print(s)
#
# # Sistema de calculo de corrida exemplo de FUNÇÃO COM PARÂMETROS:(uber)(taxi):
# # Função: retorna valor.
#
# def taximetro(distancia, multiplicador=1):
#     largada = 3
#     km_rodado = 2
#     valor = (largada + distancia * km_rodado) * multiplicador
#     return valor
#
# pagamento = taximetro(3.5)
# print(f'O pagamneto da corrida foi R$ {pagamento}')

# PROCEDIMENTOS E FUNÇÕES
print('==' * 30)
print('')

# Procedimento: São aqueles que não retornam valores.
# def func1(x):
#     x = 10
#     print(f'Função func1 - x = {x}')
#
#
# def func2(x):
#     x = 20
#     print(f'Função func2 - x = {x}')
#
#
# x = 0
# func1(x)
# func2(x)
# print(f'Programa principal - x = {x}')


# Variável Global: Ou seja dentro do método através da palavra reservada global eu mudei o valor da variavel
# def func1():
#     global x
#     x = 10
#     print(f'Função func1 - x = {x}')
#
#
# def func2(x):
#     x = 20
#     print(f'Função func2 - x = {x}')
#
#
# x = 0
# func1()
# func2(x)
# print(f'Programa principal - x = {x}')


# Subprogramas aninhados

# def taximetro(distancia):
#
#     def calculaMult():
#         if distancia < 5:
#             return 1.2
#         else:
#             return 1
#
#     multiplicador = calculaMult()
#     largada = 3
#     km_rodado = 2
#     valor = (largada + distancia * km_rodado) * multiplicador
#     return valor


# dist = eval(input("Entre com a distancia a ser percorrida em km: "))
# pagamento = taximetro(dist)
# print(f'O valor a pagar é R$ {pagamento:.2f}')

print('==' * 30)
print('')


# RECURSIVIDADE
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x - 1)


regressiva(5)


# Sequência de Fibonacci de forma Recursiva:
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(f'Fibonacci de {fatorial(5)}!')

# Sequência de Fibonacci de não Recursiva:


def fatorial(n):

    fat = 1
    if n == 0 or n == 1:
     return fat
    else:
        for x in range(2, n + 1):
            fat = fat * x
    return fat


print(f'Fibonacci: {fatorial(5)}')


# A sequência de Fibonacci é: 1, 1, 2, 3, 5, 8, 13, 21... Os dois primeiros termos são 1 e, a partir do 3º termo, cada termo é a soma dos dois anteriores.
def fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(f'Fibonacci::: {fibo(7)}')

# DOCSTRINGS: Em Python, é possível definir uma string que serve como documentação de funções definidas pelo desenvolvedor.
# Ao chamar o utilitário help() passando como parâmetro a função desejada, essa string é exibida

def fibo(n):
    'Determina o n-ésimo termo da sequência de Fibonacci'
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(help(fibo))


# A variável x da linha 6 é global. Mas, como existe outra variável com o mesmo nome dentro da função func1() – na linha 2, apenas dentro da função func1(),
# x vale 10 –, chamamos essa variável de local.
# Assim, o print da linha 7 recebe o valor da variável global (0). A execução da linha 8 chama a função func1(), que imprime o valor de x válido dentro dela (10).
# Em seguida, a execução do programa sai da função func1() e o print da linha 9 volta a enxergar a variável global x, cujo valor é 0.
def func1(x):
     x = 10
     print(x)

x = 0
print(x) # Print variavel global que vale 0
func1(x) # Aqui eu chamo o print do método que vale 10
print(x) # Print variavel global que vale 0
