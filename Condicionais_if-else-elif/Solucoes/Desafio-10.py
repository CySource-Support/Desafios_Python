# Challenge solution by Jonas
# Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou  “Boa Noite” ou “Valor inválido”, conforme o caso.

opc = input("Em qual turno vc estuda?\n[M] Matutino\n[V] Vespertino\n[N] Noturno\n>> ")
opc = opc.lower()
if opc == "m":
  print("Bom dia!")
elif opc =="v":
  print("boa tarde!")
elif opc == "n":
  print("Boa noite!")
else:
  print("Valor inválido!")

