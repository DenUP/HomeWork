# Находим факториал числа 4
# 1 Способ, через функцию
def factorial(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s
print(factorial(4))

# 2 способ, через reduce + lamda

from functools import reduce
n = 4
fact = reduce(lambda x,y:x*y, range(1,n+1))
print(fact)