def anteSuce(x):

	return x - 1, x + 1

try:

	x = int(input("Digite um número inteiro: "))

	a, s = anteSuce(x) 

	print("O antecessor de %d é %d. O sucessor, %d." % (x, a, s))

except:

	print("Você não forneceu um valor inteiro.")