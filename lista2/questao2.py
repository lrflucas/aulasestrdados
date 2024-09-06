#%%

# Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”.
# Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:

  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def detalhes(self):
    return f"O livro {self.titulo} foi escrito por {self.autor}"

titulo = input("Diga o nome do livro: ")
autor = input("Diga o nome do autor: ")
livro = Livro(titulo,autor)
detalhes = livro.detalhes()

print(livro.detalhes())

# %%