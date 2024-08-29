#%%

# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

num = int(input("Diga um número positivo: "))

for i in range(0, num + 1):
  if i % 2 == 0:
    print(i)

# %%