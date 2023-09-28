r = 'S'
soma = 0
while r == 'S':
    soma = 0
    num = int(input('Informe um número:'))
    cont = 1
    while cont < num:
        if num % cont == 0:
            soma += cont
            print(soma, cont)
        cont += 1
    if soma == num:
        print('O numero é perfeito!')
    else:
        print('Não é perfeito!')
    r = input('Deseja indicar outro número? (S/N):').upper()
    while r != 'S' and r != 'N':
        r = input('Deseja indicar outro número?(S/N):').upper()