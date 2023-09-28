num = int(input('Informe um valor inteiro positivo e par:'))
while  num % 2 != 0:
	num = int(input('Informe um valor inteiro positivo e par:'))
cont = 0
while num // 10 != 0:
	num = num // 10
	cont += 1
print(f'O numero informado tem {cont+1} digitos')
