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

def falsa_posição(a, b, ξ):
    f_a, f_b = f(a), f(b)
    x = (a * f_b - b * f_a) / (f_b - f_a)
    y = f(x)
    global i
    i += 1

    if abs(y) < ξ:
        return x
    if f_a * y > 0:
        return falsa_posição(x, b, ξ)
    else:
        return falsa_posição(a, x, ξ)

antes = time.time()
print(f"Raiz aproximada: {falsa_posição(pontoA, pontoB, tol)}")
depois = time.time()
tempo = depois - antes

print(f"Número de iterações: {i}")
print(f"Tempo necessário: {tempo}sec")

