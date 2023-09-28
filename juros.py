inv = float(input('Quanto será investido por mes?'))
jur = float(input('Qual taxa de juros mensais?'))
mont = 0
cont = 0  # para a contagem dos meses
v = 1     # ano a ser analisado, 1 = 1°ano , 2 = 2°ano...
p = True  # para poder definir o looping com um valor mutavel
while p:
    while cont < 12*v:
        mont = mont + (jur/100) * mont     # Atualizando o quanto rendeu
        mont = mont + inv                  # Atualizando o valor do montante/somando o investimento mensal
        cont += 1                          # Para a passagem dos meses
        print(f'Mês {cont}: {mont:.2f}')
    v += 1   # Atualizando o ano
    r = str  # Definindo a variavel 'r' como string
    while r != 'S' and r != 'N':           # Verificando o interesse em processar mais um ano
        r = input('Deseja processar mais um ano? (S/N):').upper()
        if r == 'N':
            p = not True                   # Nesse caso o 'while p:' passa a ser falso e o codigo para
        elif r == 'S':
            p = True
