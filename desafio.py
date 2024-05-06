menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input('Informe o valor que deseja depositar: '))
        if valor_deposito > 0 and valor_deposito <= 500:
            saldo += valor_deposito
            extrato += (f'Depósito: R${valor_deposito:.2f}')
        else:
            print('Só é possível depositar valores positivos!')

    elif opcao == "s":
        if numero_saques <= LIMITE_SAQUES:
            valor_saque = float(input('Informe o valor que deseja sacar: '))
            if valor_saque <= 500:
                numero_saques += 1
                saldo -= valor_saque
                extrato += (f'Saque: R${valor_saque:.2f}')
            else:
                print('Você só pode sacar até R$500!')
        else:
            print('Você excedeu o limite de saques!')
                
        

    elif opcao == "e":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")