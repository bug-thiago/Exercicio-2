def treze(a):

	if a >= 2013:

		return 0

	else:

		return 2013 - a

try:

	a = int(input("Digite o ano de nascimento: "))

	i = treze(a)

	if i == 0:

		print(" não nasceu.")

	else:

		print("Essa pessoa tem %d anos." % (i))

except:

	print("não forneceu um valor inteiro.")