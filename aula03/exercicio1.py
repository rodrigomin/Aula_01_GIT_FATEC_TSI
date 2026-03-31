cap = float(input("Insira a capacidade máxima do elevador [em Kg's]: "))

pessoa_1 = float(input("Insira o peso da pessoa 1: "))
pessoa_2 = float(input("Insira o peso da pessoa 2: "))
pessoa_3 = float(input("Insira o peso da pessoa 3: "))
pessoa_4 = float(input("Insira o peso da pessoa 4: "))
pessoa_5 = float(input("Insira o peso da pessoa 5: "))

total = pessoa_1 + pessoa_2 + pessoa_3 + pessoa_4 + pessoa_5

if total > cap:
    print("Limite de peso excedido")
else:
    print("Elevador liberado")