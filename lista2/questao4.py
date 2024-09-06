#%%

# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”.
# Implemente métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:

  def __init__(self, titular, saldo=0):
    self.titular = titular
    self.saldo = saldo

  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print(f"Depósito de R${valor} realizado com sucesso")
    else:
      print("Valor não é positivo")

  def sacar(self, valor):
    if valor > 0 and valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque de R${valor} realizado com sucesso")
    else:
      print(f"Valor não é suficiente ou não é positivo")


titular = input("Nome do titular: ")
valordeposito = float(input("Valor do depósito: "))
valorsaque = float(input("Valor do saque: "))
conta = ContaBancaria(titular)
conta.depositar(valordeposito)
conta.sacar(valorsaque)

print(f"O saldo da conta de {titular} atualmente é R${conta.saldo}")

# %%