#%%

# Crie uma classe chamada “Circulo” que tenha um atributo “raio”.
# Implemente um método chamado “calcular_area” que retorna a área do círculo.

class Circulo:

  pi = 3.14

  def __init__(self, raio):
    self.raio = raio

  def area(self):
    return self.pi * (self.raio ** 2)

raio = int(input("Diga o raio do círculo: "))
circulo = Circulo(raio)
area = circulo.area()

print(f"A área do círculo com raio {raio} é {area:.2f}")

# %%