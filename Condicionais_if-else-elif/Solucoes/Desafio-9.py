# Challenge solution by Jonas
# Faça um programa que leia três números e mostre-os em ordem decrescente.

# modo simplificado
print( *reversed(sorted(list(map(int, input("Informe 3 números: ").split(" "))))) )
