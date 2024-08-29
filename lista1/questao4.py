#%%

# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é {maior} e o menor é {menor}")

# %%