#%%

# Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”.
# Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:

  def calcular_area(self, base, altura):
    return base * altura

base = float(input("Diga a base do retângulo: "))
altura = float(input("Diga a altura do retângulo: "))
retangulo = Retangulo()
area = retangulo.calcular_area(base,altura)

print(f"A área do retângulo de base {base} e altura {altura} é {area:.2f}")

# %%