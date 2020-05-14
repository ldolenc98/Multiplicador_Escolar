def multiplica(a, b):

	lista_multiplicador = []
	lista_numeros = []
	i = 1
	if a > b:
		multiplicando = a
		multiplicador = b
	else:
		multiplicando = b
		multiplicador = a
	
	resultado = a*b
	resultado = str(resultado)
	multiplicador = str(multiplicador)
	multiplicando = str(multiplicando)

	for numero in multiplicador:

		lista_multiplicador.append(int(numero))

	space_multiplicador = str(" ") * (len(resultado) - len(multiplicador) )
	space_multiplicando = str(" ") * (len(resultado) - len(multiplicando) + 2)
	traco = "-" * (len(resultado) + 2)

	j = (len(multiplicador) - 1)
	while i < (len(multiplicador) + 1):

		numero = int(multiplicando) * lista_multiplicador[j]
		lista_numeros.append(numero)
		j = j - 1 
		i = i + 1
	i = 0
	string = ""
	lista_numeros.append(0)
	space = (len(traco) - len(str(lista_numeros[0])))

	while i < (len(multiplicador)):

		if i == (len(multiplicador)-1):

			space =  space - 1
			string = string + "+" + space * " " + str(lista_numeros[i]) + "\n"
			i = i + 1
		else:

			string = string + space * " " + str(lista_numeros[i]) + "\n"
			space = space - (len(str(lista_numeros[i+1])) - len(str(lista_numeros[i])) + 1)
			i = i + 1


	return  space_multiplicando + multiplicando + "\n" + "x " + space_multiplicador  + multiplicador + "\n" + traco + "\n" + string + traco + "\n" + "  " + resultado 

#print(multiplica(95682,283749))


	

		

	

	

	
