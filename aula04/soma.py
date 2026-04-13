# Exercício 1: Soma com Interrupção
# Elabore um programa em Python usando if e while que receba números digitados pelo
# usuário até que o número 0 seja digitado. Ao final, o programa deve mostrar a soma de todos
# os números inseridos (Dica: utilize o comando break).

soma = 0

while (True): 
    print("=" * 85)
    num = int(input("           Digite o número da soma [Digite 0 para finalizar o programa] \n"+ "="*85 + '\n'))
    if (num == 0):
        break

    soma+=num

print("=" * 85)
print(" "*42 + str(soma))
print("=" * 85)