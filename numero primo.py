r = 'S'
while r == 'S':
    num = int(input('Informe um número:'))
    cont = 1
    while cont <= num:
        if num % cont == 0:
            if num != cont and cont != 1:
                print('Numero nao é primo')
                break
            else:
                if cont != 1:
                    print('Numero é primo')
        cont += 1
    r = input('Deseja indicar outro número? (S/N):').upper()
    while r != 'S' and r != 'N':
        r = input('Deseja indicar outro número?(S/N):').upper()