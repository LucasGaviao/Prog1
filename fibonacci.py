n = int(input('Insira o indice do valor desejado:'))
cont = penult = ult = f = 0
while cont < n:
	if cont == 0:
		print(f'{cont}, ', end='')
	if cont == 1:
		print(f'{cont}', end='')
		ult = cont
	else:
		f = ult + penult
		penult = ult
		ult = f
		print(f'{f}, ', end='')
	cont += 1
print(f'{ult + penult}')