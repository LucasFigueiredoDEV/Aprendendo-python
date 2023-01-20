vm = 80
m = 7
v = int(input("Qual a velocidade do carro?"))
if v > 80:
    pm = v - vm
    valor = pm * m
    print("Você foi multado, e o valor da multa será de R${}.".format(valor))