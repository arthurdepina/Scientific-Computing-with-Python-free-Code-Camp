def organizacao(vetor):
    a = str(vetor[0])
    b = str(vetor[2])
    operacao = vetor[1]
    resultado = str(vetor[3])
    if len(a) >= len(b):
        n_espacos_l1 = 2
        n_espacos_l2 = len(a) - len(b) + 1
        n_tracos = len(a) + 2
        n_espacos_l4 = len(a) + 2 - len(resultado)
    else:
        n_espacos_l1 = len(b) + 2 - len(a)
        n_espacos_l2 = 1
        n_tracos = len(b) + 2
        n_espacos_l4 = len(b) + 2 - len(resultado)
    l1 = " "*n_espacos_l1 + a
    l2 = operacao + (" "*n_espacos_l2) + b
    l3 = "-"*n_tracos
    l4 = (" "*n_espacos_l4) + resultado
    return [l1, l2, l3, l4]


def arithmetic_arranger(vetor, state=False):
    if len(vetor) > 5:
        return "Error: Too many problems"
    expressoes = [""]*len(vetor)
    for i in range(len(vetor)):
        expressoes[i] = vetor[i].split()
        if not expressoes[i][0].isnumeric() or not expressoes[i][2].isnumeric():
            return "Error: Numbers must only contain digits"
        if len(expressoes[i][0]) > 4 or len(expressoes[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits"
        expressoes[i][0] = int(expressoes[i][0])
        expressoes[i][2] = int(expressoes[i][2])
        if expressoes[i][1] == "+":
            expressoes[i].append(expressoes[i][0] + expressoes[i][2])
        elif expressoes[i][1] == "-":
            expressoes[i].append(expressoes[i][0] - expressoes[i][2])
        else:
            return "Error: Operator must be '+' or '-'"
    for i in range(len(expressoes)):
        expressoes[i] = organizacao(expressoes[i])
    arranged_problems = ""
    if state:
        for i in range(4):
            arranged_problems = arranged_problems + "\n"
            for j in range(len(expressoes)):
                if j != len(expressoes) - 1:
                    arranged_problems = arranged_problems + expressoes[j][i] + "    "
                else:
                    arranged_problems = arranged_problems + expressoes[j][i]
    else:
        for i in range(len(expressoes) - 1):
            arranged_problems = arranged_problems + "\n"
            for j in range(len(expressoes)):
                if j != len(expressoes) - 1:
                    arranged_problems = arranged_problems + expressoes[j][i] + "    "
                else:
                    arranged_problems = arranged_problems + expressoes[j][i]
    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
