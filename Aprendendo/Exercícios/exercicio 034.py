s = float(input("Digite o valor do seu salário: "))
if s > 1250:
    por = s / 100
    au = por * 10
    sn = s + au
    print ("O valor do seu novo salário com o aumento de 10% é de R${}".format(sn))
else:
    porc = s / 100
    aum = porc * 15
    saln = s + aum
    print("O seu novo salário com aumento de 15% R${}".format(saln))