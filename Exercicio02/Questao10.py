def triplo(x):

	return x * 3

try:

	x = float(input("Digite um número real: "))

	print("O triplo de %f é %f." % (x, triplo(x)))

except:

	print("Você não forneceu um valor real.")