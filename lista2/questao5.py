#%%

# Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”.
# Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

nome = input("Diga o nome: ")
idade = int(input("Diga a idade: "))
pessoa = Pessoa(nome,idade)
pessoa.falar()

# %%