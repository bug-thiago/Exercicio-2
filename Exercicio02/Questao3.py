def convert(minu):

	horas = minu // 60
	mins = minu % 60

	return horas, mins

try: 

	m = int(input("valor em minutos: "))

	horas, mins = convert(m)

	print("%d minutos é equivalente a %d horas e %d minutos." % (m, horas, mins))

except:

	print("Você não forneceu um valor inteiro.")