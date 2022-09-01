#  Challenge solution by Jonas

nota = list(map(float, input("Insere notas do aluno: ").split(" ")))
media = sum(nota)/len(nota)
if media == 10:
  print("Aprovado com distinção!")
elif media >= 7:
  print("Aprovado!")
elif media < 7:
  print("Reprovado!")
else:
  print("Erro")
