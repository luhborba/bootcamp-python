while True:
    nome = input("Nome do Funcionário? ")
    if len(nome) < 1:
        print("Nome inválido")
        print("====NOVO CALCULO====")
        continue
    salario = input("Salário do Funcionário? ")
    try:
        salario = float(salario)

    except:
        print("Salário inválido")
        print("====NOVO CALCULO====")
        break
    bonus = input('Bonus do Funcionário? ')
    try:
        bonus = float(bonus)
    except:
        print("Bonus inválido")
        print("====NOVO CALCULO====")
