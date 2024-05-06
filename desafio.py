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
            extrato += (f'R${valor_deposito:.2f}')
        else:
            print('Só é possível depositar valores positivos!')

    # elif opcao == "s":
        

    # elif opcao == "e":
    #     print("\n================ EXTRATO ================")
        
    #     print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")