import random

class ImprimirNome:
    def __init__(self, nome, vezes):
        self.nome = nome
        self.vezes = vezes
        
    def imprimir(self):
        for i in range(self.vezes):
            print(self.nome)
            
class zeroToHundred:
    def __init__(self):  
        self.numero = 100
        self.soma = 0
        
    def imprimir(self):
        for i in range(self.numero + 1):
            self.soma+=i
        print(self.soma)
            
class sumParEImp:
    def __init__(self):
        self.numero = 100
        self.sumpar = 0
        self.sumimp = 0
        
    def imprimir(self):
        for i in range(self.numero + 1):
            if (i % 2 == 0):
                self.sumpar+=i
            else:
                self.sumimp+=i
                
        print(self.sumpar, self.sumimp, self.sumpar+self.sumimp)

class pairList:
    def __init__(self, min_v, max_v, div):
        self.min_v = min_v
        self.max_v = max_v
        self.div = div
        self.result = []
        
    def divList(self):
        for i in range(self.min_v, self.max_v):
            if (i % self.div == 0):
                self.result.append(i)
        return self.result
    
# inpt_nome = str(input("Digite seu nome: "))
# inpt_vezes = int(input("Vezes: "))
# ImprimirNome(inpt_nome, inpt_vezes).imprimir()

# inpt_minv = int(input("minv: "))
# inpt_maxv = int(input("maxv: "))
# inpt_div = int(input("div: "))

