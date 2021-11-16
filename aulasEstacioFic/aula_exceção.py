# CAPTURA E MANIPULAÇÃO DE EXCEÇÕES
try:
    numero = int(input('Digite um numero: '))
    print(f'Muito obrigado por digitar {numero}')
except NameError:
    print('[ERROR] É para entrar com um número e não uma letras. Tente novamente: ')
    numero = int(input('Digite um numero: '))
    print(f'Muito obrigado por digitar {numero}')

# Captura de exceções de múltiplos tipos

try:
    numero = int(input('Digite um numero: '))
    print(f'Muito obrigado por digitar {numero}')
except NameError:
    print('[ERROR] É para entrar com um número e não uma letras. Tente novamente: ')
    numero = int(input('Digite um numero: '))
    print(f'Muito obrigado por digitar {numero}')
except ValueError :
    print('Valor errado!')
except IndexError:
    print('Indice errado')
except:
    print('de novo?')