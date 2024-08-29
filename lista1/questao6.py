#%%

# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

num = int(input("Diga um número positivo: ") )

resultado = 1

for n in range(1, num+1):
    resultado = resultado * n

print(f"O fatorial de {num} é {resultado}")

# %%