#%%

# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”.
# Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:

  def __init__(self, nome, salario, cargo):
    self.nome = nome
    self.salario = salario
    self.cargo = cargo

  def aumentar_salario(self, valor):
    aumento = self.salario * (valor / 100)
    self.salario += aumento
    return f"O novo salário de {self.nome} é R${self.salario}"

nome = input("Diga o nome do funcionário: ")
salario = float(input("Diga o salário dele: "))
cargo = input("Diga o cargo dele: ")
funcionario = Funcionario(nome,salario,cargo)
valor = float(input("Diga o valor do aumento: "))
funcionario.aumentar_salario(valor)

# %%