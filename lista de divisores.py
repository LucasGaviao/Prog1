r = 'S'
while r == 'S':
    num = int(input('Informe um número:'))
    cont = 1
    while cont < num:
        if num % cont == 0:
            print(f'{cont}, ', end='')
        cont += 1
    print(num)
    r = input('Deseja indicar outro número? (S/N):').upper()
    while r != 'S' and r != 'N':
        r = input('Deseja indicar outro número?(S/N):').upper()