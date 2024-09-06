for n in range (1000, 10000):
    rest = n % 100
    div = n // 100
    raiz = rest + div
    result = raiz ** 2
    if result == n :
        print(f"Numero: {n}, menor: {rest}, maior: {div}, raiz: {raiz}")
print(f"Finalizouuuu com {n}")

import math

# Determina os limites inferior e superior
min_raiz = math.ceil(math.sqrt(1000))  # Menor raiz cujo quadrado é >= 1000
max_raiz = math.floor(math.sqrt(9999))  # Maior raiz cujo quadrado é <= 9999

for raiz in range(min_raiz, max_raiz + 1):
    n = raiz ** 2
    rest = n % 100
    div = n // 100
    soma = rest + div
    if soma == raiz:
        print(f"Numero: {n}, menor: {rest}, maior: {div}, raiz: {raiz}")

print(f"Finalizouuuu em {raiz}")
