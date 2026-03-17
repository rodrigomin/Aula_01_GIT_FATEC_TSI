def options():
    
    opcao = True
    
    while opcao != False:
        print("======================================")
        print("            CALCULADORA               ")
        print("======================================")
        print("[1] - Soma ")
        print("[2] - Subtração ")
        print("[3] - Multiplicação")
        print("[4] - Divisão")
        print("[5] - Sair")

        opcao = int(input("Escolha uma opção de 0-4 dependendo da operação que deseja: \n"))

        match opcao:
            case 1:
                somar()
            case 2:
                sub()
            case 3:
                multi()
            case 4:
                div()
            case 5:
                print("Saindo...")
                return False
            case _:
                print("Essa não é uma opção válida")
                           
 
def saindo():
    print("\n======================================")
    print("                SAINDO...              ")    
    print("====================================== \n \n")
            
def somar():
    print("\n======================================")
    print("                ADIÇÃO                ")
    print("====================================== \n")
    num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
    soma = 0
    while num != 0:
        soma+=int(num)
        num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
            
    print("\n======================================")
    print(f"           RESULTADO: {soma}           ")    
    print("====================================== \n")
    
    saindo()

    

    
def sub():
    print("\n======================================")
    print("               SUBTRAÇÃO                ")
    print("====================================== \n")
    num = 1
    sub = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
    while num != 0:
        sub-=int(num)
        num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
            
    print("\n======================================")
    print(f"           RESULTADO: {sub+1}           ")    
    print("====================================== \n")
    
    saindo()
    
def multi():
    print("\n======================================")
    print("              MULTIPLICACAO             ")
    print("====================================== \n")
    num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
    multi = 1
    while num != 0:
        multi*=int(num)
        num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
            
    print("\n======================================")
    print(f"           RESULTADO: {multi}           ")    
    print("====================================== \n")
    
    saindo()
    
def div():
    print("\n======================================")
    print("                DIVISÃO                 ")
    print("====================================== \n")
    div = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
    num = '0'
    while num != 0:
        num = int(input("Digite um número, caso queria sair e ver o resultado digite '0': "))
        if num != 0:
            div/=int(num) 
            
    print("\n======================================")
    print(f"           RESULTADO: {div}           ")    
    print("====================================== \n")
    
    saindo()
    
options()