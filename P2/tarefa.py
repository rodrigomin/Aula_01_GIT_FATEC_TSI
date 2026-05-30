# EXERCICIO 1

from random import randint

# Cria Matriz

tamanho = randint(2,10)
matriz = [[randint(0,10) for _ in range(tamanho)] for _ in range(tamanho)]


def printMatriz(which):
    for linha in which:
        print(linha)

def find_diags(which):
    diagonais = []
    n = len(which)

    for diag_i in range(n):

        diagonal_atual = []

        for i in range(n):

            j = i + diag_i

            if j < len(which[i]):
                diagonal_atual.append(which[i][j])

        if len(diagonal_atual) == n:
            diagonais.append(diagonal_atual)

    return diagonais

def reverterMatriz(which):
    reverse = []

    for i, line in enumerate(which):
        reverse.append([])

        for col in line[::-1]:
            reverse[i].append(col)

    return reverse

def multiDiags(which):
    resultado = 1

    for valor in which:
        resultado *= valor

    return resultado


reverse = reverterMatriz(matriz)

diag = find_diags(matriz)[0]
sec_diag = find_diags(reverterMatriz(matriz))[0]

# Print das Matrizes 
print("Matriz")
printMatriz(matriz)
print("\nRevertido")
printMatriz(reverse)



print("\nPrimeira Diagonal: ", diag)
print('\nSegunda Diagonal: ', sec_diag)




def determinante(matriz):
    n = len(matriz)

    if n == 1:
        return matriz[0][0]

    if n == 2:
        diag = find_diags(matriz)[0]
        sec_diag = find_diags(reverterMatriz(matriz))[0]

        return multiDiags(diag) - multiDiags(sec_diag)

    det = 0

    for col in range(n):

        menor = [] # armazena a sub matriz

        for linha in matriz[1:]:
            menor.append(
                linha[:col] + linha[col+1:]
            )
        cofator = (-1) ** col 
        det += cofator * matriz[0][col] * determinante(menor) # chama a própria função p achar o determinante da sub matriz

    return det

print("Determinante: ",determinante(matriz))