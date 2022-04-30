import math
import time
i = 0

def funcao(x):
    return 4 * math.sin(x) - math.exp(x)

def metodoSecante(x0, x1, tol):
    ponto = x1 - (funcao(x1) * (x1-x0)) / (funcao(x1) - funcao(x0))
    global i
    i += 1

    if abs(funcao(ponto)) < tol:
        return ponto
    else:
        return metodoSecante(x1, ponto, tol)

inicio = time.time()
print(f"Raiz aproximada: {metodoSecante(0, 1, 1e-5)}")
fim = time.time()
tempo = fim - inicio

print(f"Número de iterações: {i}")
print(f"Tempo necessário: {tempo}sec")