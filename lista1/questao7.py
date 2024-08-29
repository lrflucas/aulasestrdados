#%%

# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

num = int(input("Diga um número: "))

a, b = 0, 1

while a <= num:
    print(a, end=" ")
    a, b = b, a + b

# %%