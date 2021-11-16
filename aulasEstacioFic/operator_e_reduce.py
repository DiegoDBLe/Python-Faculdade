# operator é uma biblioteca
import operator
print('\nterceiro exempo: ')
print(operator.add(10, 20))


print('\nquarto exemplo: ')
from functools import reduce
print(reduce(operator.add, [10, 20]))
print(reduce(operator.concat, ['aprendendo ', ' reduce']))