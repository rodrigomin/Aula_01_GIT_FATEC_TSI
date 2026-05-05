min_val = int(input("Digite o início da lista: "))
max_val = int(input("Digite o número final da lista: "))
divisor = int(input("Digite aqui o divisor: "))


for i in range(min_val, max_val):
    if (i % divisor == 0):
        print(i)