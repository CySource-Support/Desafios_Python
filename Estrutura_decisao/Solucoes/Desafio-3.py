#  Challenge solution by Jonas

letra = input("Insert a character [F] or [M]: ")
if letra.lower() == "f":
  print(f"{letra.upper()} - Feminino  ")
elif letra.lower() == "m":
  print(f"{letra.upper()} - Masculino ")
else:
  print(f"{letra.upper()} - Incorreta ")
