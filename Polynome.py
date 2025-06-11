import random
import math

def PRODUIT(a, b):
    res = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            res[i + j] += a[i] * b[j]
    return res

def poly_en_texte(tab):
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

def racine_simple(exclus=[]):
    """Choisit une racine entière évidente ≠ 0 (dans [-5, 5])."""
    candidats = [k for k in range(-5, 6) if k != 0 and k not in exclus]
    return random.choice(candidats)

def trinome_second_degre_non_factorisable():
    """Crée un trinôme du second degré sans racine entière évidente."""
    while True:
        p = random.randint(-5, 5)
        q = random.randint(1, 6)
        D = p * p - 4 * q
        if D < 0 or int(math.isqrt(abs(D))) ** 2 != abs(D):
            return [q, p, 1]  

def generer_polynome(degre):
    """Génère un polynôme de degré 3, 4 ou 5 avec au moins une racine évidente."""

    facteurs = []

    if degre == 3:
        r = racine_simple()
        facteurs.append([-r, 1])
        facteurs.append(trinome_second_degre_non_factorisable())

    elif degre == 4:
        r1 = racine_simple()
        r2 = racine_simple(exclus=[r1])
        facteurs.append([-r1, 1])
        facteurs.append([-r2, 1])
        facteurs.append(trinome_second_degre_non_factorisable())

    elif degre == 5:
        r1 = racine_simple()
        r2 = racine_simple(exclus=[r1])
        r3 = racine_simple(exclus=[r1, r2])
        facteurs.append([-r1, 1])
        facteurs.append([-r2, 1])
        facteurs.append([-r3, 1])
        facteurs.append(trinome_second_degre_non_factorisable())

    # Multiplication des facteurs
    coeffs = [1]
    for f in facteurs:
        coeffs = PRODUIT(coeffs, f)

    texte = poly_en_texte(coeffs)
    return texte, coeffs, facteurs

# Exécution
if __name__ == "__main__":
    for d in [3, 4, 5]:
        p, c, f = generer_polynome(d)
        print(f"Degré {d} → P(x) = {p}")
