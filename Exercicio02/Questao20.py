def caixa(q):

	cin = q // 50
	dez = (q % 50) // 10
	cinc = ((q % 50) % 10) // 5
	um = q - ((cin * 50) + (dez * 10) + (cinc * 5))

	return cin, dez, cinc, um

try:

	q = int(input("Digite o valor correspondente à quantia solicitada: "))

	print("Notas de R$ 50,00: %d\nNotas de R$ 10,00: %d\nNotas de R$ 5,00: %d\nNotas de R$ 1,00: %d" % caixa(q))

except:

	print("Você não forneceu um valor inteiro.")