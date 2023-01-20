import math
ctop = float(input("Qual o comprimento do cateto oposto: "))
ctad = float(input("Qual o comprimento do cateto adjacente: "))
hip = math.hypot(ctop, ctad)
print ("Com o cateto oposto medindo {}, o cato adjacente medindo {}, o resultado da hipotenusa é de {:.2f}.".format(ctop, ctad, hip))