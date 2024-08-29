#%%

# Faça um programa que leia uma lista de números e retorne a média dos números pares.

numeros = list(map(int, input("Diga vários números e os separe por espaço: ").split()))

pares = [num for num in numeros if num % 2 == 0]

if pares:
  media = sum(pares) / len(pares)
  print(f"A média dos números pares é {media:.2f}")
else:
  print("Não há pares")

# %%