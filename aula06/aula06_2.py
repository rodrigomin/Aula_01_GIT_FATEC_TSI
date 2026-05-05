max_length = 51

print("="*max_length)
nome = str(input("Digite um nome: "))
print("="*max_length)
qnt = int(input("Quantas vezes você deseja imprimir o nome na tela?\n"))
print("="*max_length)


for i in range(qnt):
    print(nome.center(max_length))
    
print("="*max_length)