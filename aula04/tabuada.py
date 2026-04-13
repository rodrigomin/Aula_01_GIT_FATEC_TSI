# Exercício 2: Tabuada Interativa
# Elabore um programa que:
# 1. Peça um número ao usuário.
# 2. Mostre a tabuada deste número.
# 3. Pergunte se o usuário deseja exibir outra tabuada.
# 4. Se ele digitar "S" (ou "sim"), receba um novo número e repita o processo.
# 5. O programa deve encerrar apenas quando o usuário responder que não deseja mais
# continuar.


opcao = ""

while (True):
    print("="*55)
    opcao = str(input("Quer que o programa exiba uma tabuada? [y/sim ou n/nao]\n" + "="*55 + '\n'))
    print("="*55)
    
    if (opcao.lower() == "nao" or opcao.lower() == 'n'):
        break

    elif (opcao.lower() == 'sim' or opcao.lower() == 's' or opcao.lower() == 'y'):
        
        num = int(input("       Digite um número para montar a tabuada: \n" + "="*55 + '\n'))

        for i in range(10):
            print(f" {num} X {i+1} = {num*(i+1)}")

        print("="*55)
        
    else:
        print("Não existe essa opção, tente novamente.")

    

