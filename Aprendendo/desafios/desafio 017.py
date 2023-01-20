import math
cat_op = int(input("Digite o valor do cateto oposto: "))
cat_adj = int(input("Digite o valor do cateto adjacente: "))
hip = math.hypot(cat_op, cat_adj)
print("O valor da hipotenusa é de {:.2f}".format(hip))