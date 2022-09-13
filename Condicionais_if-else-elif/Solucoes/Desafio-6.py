#  Challenge solution by Jonas

num = list(map(int, input("Iserir 3 números: ").split(" ")))
maior = 0
for i in num:
  if i > maior:
    maior = i
print(maior)
