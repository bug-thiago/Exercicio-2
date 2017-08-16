def net(n, e, t):

	print("\n\nNome: %s.\nEndereço: %s.\nTelefone: %s." % (n, e, t))

try:

	n, e, t = input("Digite:\n\nNome: "), input("Endereço: "), input("Telefone: ")

	net(n, e, t)

except:

	print("Você não forneceu os dados.")