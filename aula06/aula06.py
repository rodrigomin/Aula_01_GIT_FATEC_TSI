class olaMundo:
    def __init__(self, nome, amante):
        self.nome = nome
        self.amante = amante
    
    def teste(self):
        return f'ola {self.amante}, você é amante do {self.nome}'

ex = olaMundo('Eduardo', 'Rodrigo')
ex1 = olaMundo('Rodrigo', 'Eduardo')
ex2 = olaMundo('Eduardo', 'Rodrigo')
print(ex.teste())