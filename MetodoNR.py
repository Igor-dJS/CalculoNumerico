import math
import time
i = 0


def f(x):
    return 4 * math.sin(x) - math.exp(x)

def fder(x):
    return 4 * math.cos(x) - math.exp(x)

def metodoNR(x0, tol):
    x1 = x0 - f(x0) / fder(x0)

    global i
    i += 1

    print(f"x1: {x1}")
    print(f"f(x1): {f(x1)}")

    

    if abs(f(x1)) < tol:
        return x1
    else:
        return metodoNR(x1, tol)


antes = time.time()
print(f"Raiz aproximada: {metodoNR(0, 1e-5)}")
depois = time.time()
tempo = depois - antes

print(f"Número de iterações: {i}")
print(f"Tempo necessário: {tempo}sec")