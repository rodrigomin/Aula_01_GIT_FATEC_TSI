print("==================================================")
print("                       AREAS                      ")
print("==================================================\n")

print("[1] - Área do Retângulo")
print("[2] - Área do Triângulo\n")

print("==================================================\n")


op = int(input("Digite a opção: \n"))

print("==================================================\n")

if op == 1:
    base = float(input("Agora digite a base - "))

    altura = float(input("Agora digite a altura - "))
    
    area = base*altura
    
    print("\n==================================================\n")
    print(f"            RESULTADO RETANGULO --> {area}        \n")
    print("==================================================\n")
    
elif op == 2:
    base = float(input("Agora digite a base - "))

    altura = float(input("Agora digite a altura - "))
    area = (base*altura)/2
    print("\n==================================================\n")
    print(f"             RESULTADO TRIÂNGULO --> {area}        \n")
    print("==================================================\n")
else:
    print("Erro: Opção inválida")
