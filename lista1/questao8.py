#%%

# Faça um programa que determine se um número é primo ou não.

num = int(input("Diga um número: "))

if num < 2:
    print(f"{num} não é primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")

# %%