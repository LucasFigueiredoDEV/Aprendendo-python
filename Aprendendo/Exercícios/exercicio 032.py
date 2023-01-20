print("Descubra se o ano é bissexto")
a = int(input("Digite um ano: "))
if a % 4 == 0 and a %100!= 0:
    print("O ano {} é um ano bissexto!".format(a))
else:
    print("O ano {} não é um ano bissexto!".format(a))