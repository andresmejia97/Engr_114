from math import factorial, sin, radians

def taylor_exp_e(x,n):
    approx = 0
    for i in range(n):
        term = x**i/factorial(i)
        approx = approx + term
    return approx

def taylor_exp_sin(x,n):
    approx = 0
    for i in range(n):
        term = (-1)** n * (x**(2* n + 1)/factorial(2* n + 1))
        approx = approx + term
        return approx