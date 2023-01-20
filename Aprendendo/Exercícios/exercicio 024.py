#printando para descobrir se tal palavra existe no inicio da frase#
cidade = input("Digite o nome da sua cidade: ")
d = cidade.split()
print ("O nome da sua cidade possue a palavra 'Santo': {}".format("Santo" in d[0] ))