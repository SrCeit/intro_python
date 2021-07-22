def cuadrado(n):
    return(n**2)

def cubo(n):
    return(n**3)

def enesima(m, n):
    return(m**n)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result