#%%

# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador.
# O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.

import random

pessoa = input("Escolha pedra, papel ou tesoura: ").lower()

pc = random.choice(['pedra', 'papel', 'tesoura'])
print(f"O computador escolheu: {pc}")

if pessoa == pc:
    print("Empate!")
elif (pessoa == 'pedra' and pc == 'tesoura') or \
     (pessoa == 'papel' and pc == 'pedra') or \
     (pessoa == 'tesoura' and pc == 'papel'):
    print("Você ganhou!")
else:
    print("O computador ganhou!")
    
# %%