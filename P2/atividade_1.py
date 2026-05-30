def mainController(parcel: float, rend: float, score: int):

    prct = parcel / rend * 100
    if (prct >= 30.00):
        return '1 Crédito Negado'
    elif (score <= 300):
        return '2 Crédito Negado'
    elif (score >= 300 and score <= 500 and prct <= 15.00):
        return '3 Crédito Aprovado'
    elif (score > 500 and score < 700 and prct <= 30.00):
        return '6 Crédito Aprovado'
    elif (score >= 700 and prct <= 40.00):
        return '4 Crédito Aprovado Premium'
    else:
        return '5 Crédito Negado'


def main():
    max_w = 85

    print('='*max_w)
    rend_m = float(input("Digite sua renda mensal aqui: "))
    credit = int(input("Sua pontuação de crédito (Score) [0 - 1000]: "))
    par_value = float(input("Qual o valor das parcelas? "))
    print('='*max_w, '\n')


    res = mainController(par_value, rend_m, credit)
    
    return print('='*max_w), print(res), print('='*max_w)

main()

