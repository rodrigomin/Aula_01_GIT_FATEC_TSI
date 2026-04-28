while True:
    num = int(input("Digite um valor para a tabuada: "))
    if num == 0:
        print("0 = encerrar")
        break
    nMin = int(input("Digite o valor minimo para a tabuada: "))
    nMax = int(input("Digite o valor maximo para a tabuada: "))
    print(f"Tabuada do {num} de {nMin} até {nMax}")
    
    i = nMin
    while i <= nMax:
        res = num * i
        print(f"{num} X {i} = {res}")
        i+=1