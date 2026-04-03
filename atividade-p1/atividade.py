# FAZER UMA APLICAÇÃO QUE CALCULE O IMPOSTO DE RENDA DE UMA PESSOA
# JÁ QUE O IMPOSTO DE RENDA VARIA DEPENDENDO DO SALÁRIO
# REDUÇÃO E IMPOSTO DE RENDA (SÃO 2 TABELAS DIFERENTES)

# use esse site https://www.gov.br/secom/pt-br/acompanhe-a-secom/noticias/2026/01/nova-tabela-do-ir-veja-faixas-e-aliquotas-e-saiba-mais-sobre-medida-que-isenta-o-pagamento-para-quem-ganha-ate-r-5-mil

def reducao(renda):
    if renda < 5000:
        return 312.89
    elif (renda >= 5000.01 and renda < 7350):
        return 978.62 - (0.133145 * renda)
    elif (renda > 7350.01):
        return 0
    else:
        return 0
    
def imposto(esc):
    match (esc):
        case 0:
            
            print('\n')
            print("===================================================================== \n")
            
            renda = float(input("Insira sua renda mensal aqui: \n"))
            
            print("==================================================================== \n")

            if (renda <= 2428.80):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao if deducao >= 0 else 0
                
                rendaliquida = renda - deducao
                return ("Seu imposto de renda é " + str(deducao) + " e sua Renda Líquida é " + str(rendaliquida))
            elif (renda > 2826.66 and renda <= 3751.05):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao if deducao >= 0 else 0
                
                rendaliquida = renda - deducao
                return ("Seu imposto de renda é " + str(deducao) + " e sua Renda Líquida é " + str(rendaliquida))
            elif (renda > 3751.06 and renda <= 4664.68):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao if deducao >= 0 else 0
                
                rendaliquida = renda - deducao
                return ("Seu imposto de renda é " + str(deducao) + " e sua Renda Líquida é " + str(rendaliquida))
            elif (renda > 4664.68):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao if deducao >= 0 else 0
                
                rendaliquida = renda - deducao
                return ("Seu imposto de renda é " + str(deducao) + " e sua Renda Líquida é " + str(rendaliquida))
            
        case 1:
            renda = float(input("Insira sua renda mensal aqui: \n"))
            if(renda <= 2428.80):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao*=12
                rendaliquida = (renda*12) - deducao
                return ("Seu imposto de renda anual é " + str(deducao) + " e sua Renda Líquida Anual é " + str(rendaliquida))
            elif (renda > 2826.66 and renda <= 3751.05):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao*=12
                rendaliquida = (renda*12) - deducao
                return ("Seu imposto de renda anual é " + str(deducao) + " e sua Renda Líquida Anual é " + str(rendaliquida))
            elif (renda > 3751.06 and renda <= 4664.68):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao*=12
                rendaliquida = (renda*12) - deducao
                return ("Seu imposto de renda anual é " + str(deducao) + " e sua Renda Líquida Anual é " + str(rendaliquida))
            elif (renda > 4664.68):
                red = reducao(renda)
                deducao = (renda * 0.15) - red
                deducao*=12
                rendaliquida = (renda*12) - deducao
                return ("Seu imposto de renda anual é " + str(deducao) + " e sua Renda Líquida Anual é " + str(rendaliquida))
        case 2:
            print("==================================================================== \n")
            print("                              SAINDO...                               \n ")
            return "==================================================================== \n"

        case _:
            return "Não existe essa opção, tente novamente"
            
escolha = int(0)

while (escolha != 2):
    print("====================================================================")
    print("                    CALCULADORA DE IMPOSTO DE RENDA                 ")
    print("==================================================================== \n")
    print("[0] - Imposto de Renda Mensal")
    print("[1] - Imposto de Renda Anual")
    print("[2] - Sair \n")
    print("==================================================================== \n")

    escolha = int(input("Digite a opção que deseja: \n"))
    print(imposto(escolha))

