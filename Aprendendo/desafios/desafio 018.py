import math
ang = int(input("Digite o valor de um angulo qualquer: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print ("O valor do seno é de {}, do cosseno é de {}, e da tangente é de {}.".format(seno, cosseno, tangente))