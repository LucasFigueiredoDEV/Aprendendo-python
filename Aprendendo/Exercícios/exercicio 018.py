import math
ang = int(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print("Com o valor do angulo medindo {}, o valor do seno é de {}, do cosseno é de {} e da tangente é de {}.".format(ang, seno, cosseno, tangente))