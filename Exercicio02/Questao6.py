def KmToM(k):

	return k / 3.6

try:

	k = float(input("Digite o valor correspondente à medida em km/h: "))

	print("%f km/h correspondem a %f m/s." % (k, KmToM(k)))

except:

	print("Você não forneceu um valor real.")