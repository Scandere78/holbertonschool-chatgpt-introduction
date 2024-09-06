#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Le nombre doit être non négatif.")
except ValueError as e:
    print(f"Erreur : {e}")
    sys.exit(1)

f = factorial(number)
print(f)
