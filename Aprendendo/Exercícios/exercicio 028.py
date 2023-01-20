import random
num = int(random.randint(0, 5))
n = int(input("Digite um número de 0 a 5: "))
if n == num:
    print("Você acertou!")
else:
    print("Você errou, o computador venceu!")