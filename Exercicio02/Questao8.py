def div(x, y):

	q = x // y
	r = x % y

	return q, r

try:

	x, y = int(input("Digite dois números inteiros: ")), int(input())

	q, r = div(x, y)

	print("O quociente da divisão de %d por %d é %d. O resto, %d." % (x, y, q, r))

except:

	print("Você não forneceu valores inteiros.") 