import math
import numpy as np
import sympy

x = sympy.Symbol('x')

function = math.e**-x

value = 0
count = 0
error = 0
last_f_prime = function

point = 0.755
base = 0.75

expected = function.subs(x, point)

def FuncionTaylor(value, count, function, last_f_prime, point, base):

    if (count==0):
        value1 = last_f_prime.subs(x, base)
        return value1, last_f_prime

    else:
        fprime = last_f_prime.diff()
        value1 = value + ( ( (fprime.subs(x, base)) / (math.factorial(count)) ) * math.pow(point - base, count) )
        return value1, fprime

def ErrorRelativo(va, ve):
    
    error = abs((va-ve)/ve)*100
    return error

# Main
for i in range(0, 16):
    
    value, last_f_prime = FuncionTaylor(value, count, function, last_f_prime, point, base)
    count = count + 1
    error = ErrorRelativo(value, expected)
    
    print(
        ""
        f"\nIteración {count}" +
        f"\nValor obtenido: {value}" +
        f"\nValor esperado: {expected}" +
        f"\nError relativo porcentual: {error}" +
        ""
    )