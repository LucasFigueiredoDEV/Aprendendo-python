C = 1
F = 2
perg = int(input("Digite 1 se a sua temperatura local está em Celsius ou 2 se está em Fahrenheit: "))
if perg == 1:
     tc = float(input("Informe a sua temperatura em celsius: "))
     trans_c = ((9*tc)/5)+32
     print ("A sua temperatura em Fahrenheit é de {}F°.".format(trans_c))
if perg == 2:
     tf = float(input("Digite a sua temperatura em fahrenheit: "))
     trans_f = ((tf - 32)*5)/9
     print ("A sua temperatura em celsius é de {}C°.".format(trans_f))