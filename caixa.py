menu = """  
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
 """
LIMITE_SAQUES = 3
saldo = 0
numero_de_saques = 0
limite_por_saque = 500
extrato = ""

while True:
    opção = int(input(menu))
    if opção == 1:
        deposito = int(input('Quantos Você deseja depositar?'))
        if deposito <=0:
            print('Valor inválido, por favor deposite um valor superior a 0')
        else:
            saldo += deposito
    elif opção == 2:

        valor = int(input('Quantos Deseja Sacar?'))

        if  numero_de_saques >= LIMITE_SAQUES:
            print('Quantidade diária de saque excedeu')
        elif valor > saldo:
            print('Você não possui saldo suficiente')
        elif valor > limite_por_saque:
            print('O limite de saque é 500 por vez')
        elif valor >0:
            saldo -= valor
            numero_de_saques += 1
        else:
            print('Operação falhou, o valor informado é inválido.')
    elif opção == 3:
        print('Seu saldo atualmente é {}'.format(saldo))
    elif opção == 4:
        print('Saindo do sistema.')
        break
    else:
        print('Opção inválida. Escolha uma opção válida do menu.')