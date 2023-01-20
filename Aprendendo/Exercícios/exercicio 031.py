vm = 0.45
vmm = 0.50
d = int(input("Qual a distância da sua viagem em KM? "))
p = d * vm
pp = d * vmm
if d > 200:
    print ("O valor da sua passagem será de R${}.".format(p))
else:
    print ("O valor da sua passagem será de R${}.".format(pp))