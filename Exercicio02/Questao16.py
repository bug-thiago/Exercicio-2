def quadrado(l):

	return l * l, l * 4

try:

	l = float(input("Digite o valor correspondente à medida do lado do quadrado: "))

	a, p = quadrado(l)

	print("A área desse quadrado é %f. O perímetro, %f." % (a, p))

except:

	print("Você não forneceu um valor real.")