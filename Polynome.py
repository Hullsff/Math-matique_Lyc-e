import random
import math

def PRODUIT(a, b):
    res = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            res[i + j] += a[i] * b[j]
    return res

def afficher(tab):
    deg = len(tab) - 1
    s = ""
    for i in range(len(tab)):
        coef = tab[-(i + 1)]
        if coef == 0:
            continue
        p = deg - i
        signe = "+" if coef > 0 else "-"
        abscoef = abs(coef)

        if s == "":
            if signe == "-":
                s += "-"
        else:
            s += " " + signe + " "

        if p == 0:
            s += str(abscoef)
        elif p == 1:
            s += f"{'' if abscoef == 1 else abscoef}x"
        else:
            s += f"{'' if abscoef == 1 else abscoef}x^{p}"
    return s if s else "0"

def racine():
    return random.choice([k for k in range(-5, 6) if k != 0])

def trinome():
    while True:
        p = random.randint(-5, 5)
        q = random.randint(1, 6)
        D = p * p - 4 * q
        if D < 0 or int(math.isqrt(abs(D))) ** 2 != abs(D):
            return [q, p, 1]

def generer(degre):
    facteurs = []

    if degre == 3:
        facteurs.append([-racine(), 1])
        facteurs.append(trinome())

    elif degre == 4:
        facteurs.append([-racine(), 1])
        facteurs.append([-racine(), 1])
        facteurs.append(trinome())

    elif degre == 5:
        facteurs.append([-racine(), 1])
        facteurs.append([-racine(), 1])
        facteurs.append([-racine(), 1])
        facteurs.append(trinome())

    coeffs = [1]
    for f in facteurs:
        coeffs = PRODUIT(coeffs, f)

    return afficher(coeffs), coeffs, facteurs

# Exemple
for d in [3, 4, 5]:
    p, _, _ = generer(d)
    print(f"Degré {d} → P(x) = {p}")
