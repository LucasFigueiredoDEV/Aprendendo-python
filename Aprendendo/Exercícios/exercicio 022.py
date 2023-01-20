nome = input("Qual o seu nome?")
# printando com todas as letras maiusculas #
print ("O seu nome com todas as letras maiusculas ficaria: {}".format(nome.upper()))
# printando com todas as letras minusculas #
print ("O seu nome com todas as letras minusculas ficaria: {}".format(nome.lower()))
# printando cortando os espaços #
print ("O seu nome cortando espaços desnecessários possue {} carácteres".format(len(nome.strip())))
# printando e contando quantas letras tem o primeiro nome #
dividido = nome.split()
print ("O seu primeiro nome possue {} letras".format(len(dividido[0])))