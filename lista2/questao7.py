#%%

# Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”.
# Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"O carro é da marca {self.marca}, modelo {self.modelo}, e de {self.ano}"

marca = input("Diga a marca do carro: ")
modelo = input("Diga o modelo do carro: ")
ano = int(input("Diga o ano do carro: "))
carro = Carro(marca,modelo,ano)
detalhes = carro.detalhes()

print(detalhes)

# %%