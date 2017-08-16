def trocar(a, b):

	a, b = b, a

	return a, b

try:

	a, b = float(input("Digite dois valores reais: ")), float(input())

	c, d = trocar(a, b)

	print("%f\n%f" % (c, d))

except:

	print("Você não forneceu valores reais.")