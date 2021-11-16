# Funções Lambda: criação de funções anônimas, são definidas sem identificador (ou nome) e, normalmente, são utilizadas como argumentos para
# outras funções (de ordem superior) Para criá-las, utilizamos a seguinte sintaxe:  lambda argumentos: expressão

# Exemplo de função imperativa:
def multiplica(a, b):
    return a * b


print(multiplica(2, 5))


# Exemplo de função lambda
lam = lambda a, b: a * b
print('Lambda ->', lam(5, 2))


# Exemplo de uma função normal:
def multiplica_por(multiplicador):

    def multi(multiplicando):

        return multiplicando * multiplicador

    return multi


multiplicador_por_10 = multiplica_por(10)
print(multiplicador_por_10(1))
print(multiplicador_por_10(2))

multiplicador_por_5 = multiplica_por(5)
print(multiplicador_por_5(1))
print(multiplicador_por_5(2))


# Agora a def multi usando lambda
def multiplica_porL(multiplcador):
    return lambda multiplicando: multiplicando * multiplcador


multiplicador_por_10 = multiplica_porL(10)
print('Lambda ->', multiplicador_por_10(1))
print('Lambda ->', multiplicador_por_10(2))

multiplicador_por_5 = multiplica_porL(5)
print('Lambda ->', multiplicador_por_5(1))
print('Lambda ->', multiplicador_por_5(2))
