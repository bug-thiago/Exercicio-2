def verificar(n):

	num = str(n)

	if len(num) == 3:

		return num

	else:

		return 0

n = int(input("Digite um número de três algarismos: "))

if verificar(n) == 0:

	print("Você não forneceu um número de três algarismos.")

else:

	print(verificar(n)[::-1])