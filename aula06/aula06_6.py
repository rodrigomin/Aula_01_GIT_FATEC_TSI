import random

while True:
    num = random.randint(0, 10)
    num2 = random.randint(0, 10)    
    
    print("Qual o resultado da operação: ")
    print(f' {num} X {num2} = ? ')  

    inpt_result = int(input("Digite o resultado dessa divisão: "))  
    
    if (inpt_result == (num * num2)):
        print("Acertou!")
        break
    elif (inpt_result == 0):
        print("Finalizando programa...")
        break
    else:
        print("Errou")