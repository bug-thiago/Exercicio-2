def expr(x, y):

	return (x + y) / (x - y)

try:

	x = float(input("Digite dois valores reais: "))
	y = float(input())

	print(expr(x, y))

except:

	print("Você não forneceu valores reais.")