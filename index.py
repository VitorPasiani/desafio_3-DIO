class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


    def atacar(self):
        if self.tipo == "mago":
            atacar = "magia"
    
        elif self.tipo == "guerreiro":
            atacar = "espada"
    
        elif self.tipo == "monge":
            atacar = "artes marciais"

        elif self.tipo == "ninja":
            atacar = "shuriken"

        return f"{self.tipo} atacou com {atacar}"

# --- VALIDAÇÃO --- #

mago_heroi = heroi("Harry Potter", 11, tipo="mago")

ninja_heroi = heroi("Naruto Uzumaki", 16, tipo="ninja")

print("--- Teste de Ataques ---")

print(mago_heroi.atacar())

print(ninja_heroi.atacar())
    