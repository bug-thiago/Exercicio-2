def mToKm(m):

	return m * 3.6

try:

	m = float(input("Digite um valor correspondente à medida em m/s: "))

	print("%f m/s correspondem a %f km/h." % (m, mToKm(m)))

except:

	print("Você não forneceu um valor real.")