soma_impares = 0
cont_impares = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    if numero % 2 != 0:
        soma_impares +=numero
        cont_impares +=1
        print(soma_impares, cont_impares)

# fim do if
    media = soma_impares / cont_impares
    print("A média dos ímpares é: ", media)
    
    
"""
        O problema é: caso o primeiro número inserido não for impar, ele não conta nada, posteriormente tenta dividir
    por 0 (causando o ZeroDivisionError: division by zero), já q nenhum valor impar foi inserido. Também tem o erro do
    while, o input só é chamado uma vez, e é fora do loop, oq causa um looping infinito, já que numero nunca poderá ser
    diferente uma vez definido.
"""