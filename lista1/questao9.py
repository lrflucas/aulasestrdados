#%%

# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = ["Miguel", "Davi", "André", "Ana", "Amanda", "Beatriz", "Carlos", "Arthur", "Laura", "Cinthia", "Alice", "Sophia", "Camila", "Lucas", "Alan", "Alexandre", "Pedro"]

nomesa = [nome for nome in nomes if nome[0] == 'A']

print(nomesa)

# %%