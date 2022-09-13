#  Challenge solution by Jonas
#  Faça um programa que leia três números, verifique (usando if e else) e mostre o maior e o menor deles;

num1 = int( input(" 1° numero: "))
num2 = int( input(" 2° numero: "))
num3 = int( input(" 3° numero: "))
if num1 < num2 > num3:
  print(num2)
elif num2 < num1 > num3:
  print(num1)
elif num2 > num3 > num1:
  print(num3)
