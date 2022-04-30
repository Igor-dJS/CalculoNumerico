import math
import time
i = 0

func = input("Digite a função seguindo a sintaxe Python: ")
tol = float(input("Tolerancia? "))
print()

pontoA = float(input("Primeiro ponto (deve ser menor que o próximo): "))
pontoB = float(input("Segundo ponto (deve ser maior que o anterior): "))
print()

def f(x):
    return eval(func)


def bissecção(a, b, ξ):
    x = (a + b) / 2
    y = f(x)

    global i
    i += 1


    if abs(y) < ξ:
        return x
    if f(a) * y > 0:
        return bissecção(x, b, ξ)
    else:
        return bissecção(a, x, ξ)


antes = time.time()
print(f"Raiz aproximada: {bissecção(pontoA, pontoB, tol)}")
depois = time.time()
tempo = depois - antes

print(f"Número de iterações: {i}")
print(f"Tempo necessário: {tempo}sec")
        

