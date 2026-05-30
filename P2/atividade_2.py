def conjectCollatz(num):
    process = []
    while (num != 1):

        if (num % 2 == 1):
            num = num*3 + 1

        num = num / 2
        print(num)
        process.append(num)


    return process

def main():
    num = int(input("Digite um número inteiro positivo: "))

    if (num < 0):
        return print("Esse número não é positivo")
    else:
        return print(conjectCollatz(num))


main()