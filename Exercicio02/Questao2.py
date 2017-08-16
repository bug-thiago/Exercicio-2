try:

	def calcPorcent(v):

		return v * 0.7

    x = float(input("Digite um valor em real (R$): "))


	print("70%c de %f é %f." % ("%", x, calcPorcent(x)))

except:

	print("Você não forneceu um valor real.")