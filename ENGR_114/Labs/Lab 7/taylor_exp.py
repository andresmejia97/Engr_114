from math import factorial, sin, radians

def taylor_exp_e(x,n_int):
    approx = 0
    for i in range(n_int):
        term = x**i/factorial(i)
        approx = approx + term
    return approx

def taylor_exp_sin(x,n_int):
    approx = 0
    x = radians(x)
    for i in range(n_int):
        term = (-1)** n_int * (x**(2*n_int + 1)/factorial(2* n_int + 1))
        approx = approx + term
        return approx