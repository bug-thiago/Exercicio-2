def min(hh, mm):

	return (hh * 60) + mm

try:

	hh, mm = float(input("Digite o valor correspondente à hora atual: ")), float(input("Forneça o valor correspondente ao minuto atual: "))

	print("Se passaram %d minutos desde o início do dia." % min(hh, mm))

except:

	print("Você não forneceu valores reais.")