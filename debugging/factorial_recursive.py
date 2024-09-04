#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérification du nombre d'arguments
if len(sys.argv) < 2:
    print("Usage: python3 script.py <non-negative integer>")
    sys.exit(1)

try:
    # Conversion de l'argument en entier
    n = int(sys.argv[1])
    
    # Vérification que le nombre est non négatif
    if n < 0:
        raise ValueError("Le nombre doit être un entier non négatif.")
    
    # Calcul du factoriel
    f = factorial(n)
    print(f)
except ValueError as e:
    print(f"Erreur : {e}")
    sys.exit(1)

