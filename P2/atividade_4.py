from random import randint

max_w = 85

def voteLoop(candidatos):
    votos = []
    cont = [0]*4 # 3 candidatos + o nulo

    while True:
        inpt = str(input('\n' + '='*max_w + "\nDigite o seu voto aqui [Digite 'fim' para finalizar a votação] ----> ")).lower()
        print('='*max_w)

        if (inpt == "fim"):
            break

        votos.append(inpt)


    for voto in votos:
        if (voto in candidatos):
            cont[candidatos.index(voto)]+=1 # voto contabiliza conforme a index do cont
        else:
            cont[3]+=1 # voto nulo

    print('='*max_w)
    print(f"E os votos foram: \n[{cont[0]}] - {candidatos[0]}\n[{cont[1]}] - {candidatos[1]}\n[{cont[2]}] - {candidatos[2]}\n[{cont[3]}] - Voto Nulo")
    print('='*max_w)

    # decide vencedor
    st = cont[0]
    saveI = 0
    for i, qnt in enumerate(cont[1::2]):
        if (st < qnt):
            qnt = st
            saveI = i
        elif (st == qnt):
            randomizar = randint(0,1)

            if (randomizar == 0):
                st = st
            else:
                st = qnt

            saveI = i
    
    print('\n' + '='*max_w)
    print(f"O Vencedor é {candidatos[saveI]} - com {cont[saveI]} votos!")
    print('='*max_w)

            

def main():
    candidatos = [str(input('='*max_w + '\nDigite o nome de um candidato: ')).lower() for _ in range(3)]
    print('='*max_w, '\n')

    voteLoop(candidatos)


main()