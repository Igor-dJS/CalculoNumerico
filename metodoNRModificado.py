import math
import time

i = 0

# definindo a função
def f(x):
    return x * math.log(x, 10) - 1

#derivada da função
def fder(x):
    return math.log(x, 10) + 1/(math.log(10))

def metodoNR(x0, tol, tolDerivada):
    derivada = fder(x0)

    while abs(f(x0)) > tol:
        global i
        i += 1


        if abs(fder(x0)) > tolDerivada:
            derivada = fder(x0)
        else:
            derivada = derivada

       #if i >=5000:
            #return x0, f(x0)

        x0 = x0 - f(x0) / derivada

    return x0, f(x0)


antes = time.time()
print(f"Raiz aproximada e valor da função na raiz: {metodoNR(2, 1e-16, 1e-2)}")
depois = time.time()
tempo = depois - antes

print(f"Número de iterações: {i}")
print(f"Tempo necessário: {tempo}sec")
