calculo = int(input("=============================\nVocê quer saber o volume da caixa de papelão ou da lata de óleo? \n============================= \n [0] - Caixa de Papelão \n [1] - Lata de Óleo \n==============================\n"))


if calculo == 0:
    altura = float(input("Digite aqui a altura da caixa - "))
    largura = float(input("Digite aqui a largura da caixa - "))
    comprimento = float(input("Digite aqui o comprimento da caixa - "))

    resultado = altura * largura * comprimento
    print("\nO volume da caixa de papelão é: ", resultado)  
elif calculo == 1:
    pi = 3.14159
    raio = float(input("Digite aqui o raio da lata de óleo - "))
    altura = float(input("\nDigite aqui a altura da lata de óleo - "))
    
    resultado = pi*(raio**2)*altura

    print("\nO volume da lata de óleo é aproximadamente: ", round(resultado))
else:
    print("\n \nNão existe essa opção")