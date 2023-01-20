s = float(input("Qual o salário do funcionário? R$"))
sp = s / 100 * 15
sr = s + sp
print ("Com o ajuste de salário de mais 15%, um funcionário que ganhava R${}, vai passar a ganhar R${}.".format(s, sr))