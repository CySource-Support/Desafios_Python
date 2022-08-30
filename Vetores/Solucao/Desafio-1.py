# Challenge solution by Jonas

from random import randint

vetor = [randint(1,100) for a in range(12)]
x = randint(0, 11)
y = randint(0, 11)
print(*vetor)
print(f"{vetor[x]} + {vetor[y]} = {vetor[x] + vetor[y]}")
