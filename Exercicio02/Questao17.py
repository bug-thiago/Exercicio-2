def desconto(pr, p):

	return pr - (pr * (p / 100))

try:

	pr, p = float(input("Digite o valor correspondente ao preço do produto e o valor correspondente ao percentual de desconto: ")), float(input())

	print("O preço do produto é %f." % (desconto(pr, p)))

except:

	print("Você não forneceu valores reais.")