'''
    Taylor Polynomial Producer and Grapher
    by Tony Valencia
'''

import sympy as sym
import matplotlib.pyplot as plt

def create_taylor_polynomial(order: int, center: float, variable: sym.Symbol, function):
    '''
        Creates a Taylor series given an order [N] and function [f(x)]

        Taylor polynomials are defined as:

            f(x) = a0 + a1(x-a) + a2(x-a)(x-a) + a3(x-a)(a-x)(x-a) + ...

            where aN is the order of the polynomial and is calculated by:

            aK = fK(a) / k!

        The loop below first calculates a0 of the polynomial then
        calculates the subsequent aN terms for a given order using
        the above Taylor polynomial formula.
    '''
    Sum = function.subs(variable, center)   # a0 calculation
    for i in range(1, order+1):             # order+1 because stop value of range is not inclusive
        function = sym.diff(function)
        expr = (function.subs(variable, center) / sym.factorial(i)) * (variable - center)**i
        Sum = expr + Sum
    return Sum

def graph_polynomial(original_function, polynomial, variable):
    x = [i for i in range(-4, 4 + 1)]
    original_function_eval = [original_function.subs(variable, i) for i in x]
    polynomial_eval = [polynomial.subs(variable, i) for i in x]

    print(f'function: {original_function}')
    print(f'x_values: {x} \n\t y_values: {original_function_eval}\n')
    print(f'polynomial: {polynomial}')
    print(f'x_values: {x} \n\t y_values: {polynomial_eval}')

    plt.plot(x, original_function_eval, x, polynomial_eval)
    plt.show()

if __name__ == '__main__':

    x = sym.Symbol('x')
    b = sym.sin(x)
    c = create_taylor_polynomial(4, 1.0, x, b)
    print(f'output polynomial: {b}') 

    graph_polynomial(b, c, x)
