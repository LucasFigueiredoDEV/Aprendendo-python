print("""A frase que você digitar servirá para descobrir quantas vezes a letra 'A' aparece na frase
Quando a letra 'A' apareceu pela primeira vez
Quando a letra 'A' apareceu pela última vez""")

frase = input("Digite uma frase: ")
print ("A letra 'A' aparece {} vezes na sua frase".format(frase.count("A")))
print ("A letra 'A' apareceu pela primeira vez na sua frase no caráctere {}".format(frase.find("A")))
print ("A letra 'A' apareceu pela última vez na sua frase no caráctere {}".format(frase.rfind("A")))