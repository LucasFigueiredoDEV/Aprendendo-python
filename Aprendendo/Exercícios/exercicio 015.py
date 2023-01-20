d = 60.0
quil = 0.15
dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros foram rodados? "))
vd = d * dias
vquil = quil * km
vf = vd + vquil
print ("O valor total a pagar pelo valor do carro é de R${}".format(vf))