i = 1
max_line = 45

while i != 0:
    print('\n')
    print("=" * max_line)
    num = int(input("De qual número você deseja a tabuada? "))
    print(f'{'='*max_line}')
    i = int(input("Você quer que a tabuada se extenda até que número? "))
    print(f'{'='*max_line}')
    temp = 0
    
    print('\n')
    print("=" * max_line)
    while temp <= i:
        print(f"{num} X {temp} = {num*temp}")
        temp+=1
    print("=" * max_line)

    print("Deseja continuar? [y(sim)/n(nao)]")
    print("=" * max_line)
    opcao = str(input("\n"))
    
    match opcao.lower():
        case 'y':
            continue
        case 'n':
            print("=" * max_line)
            print("Finalizando...")
            print("=" * max_line)
            i = 0
            break
        case 'sim':
            continue
        case 'nao':
            print("=" * max_line)
            print("Finalizando...")
            print("=" * max_line)
            i = 0
            break
        case _:
            print("=" * max_line)
            print("Não existe essa opção, a aplicação vai continuar")
            print("=" * max_line)
            break