def mp(x, y, w, z):

	return (x + (y * 2) + (w * 3) + (z * 4)) / 10

try:

	a, b, c, d = float(input("Digite quatro números reais: ")), float(input()), float(input()), float(input())

	print("A média ponderada dos números fornecidos é %f." % (mp(a, b, c, d)))

except:

	print("Você não forneceu valores reais.") 