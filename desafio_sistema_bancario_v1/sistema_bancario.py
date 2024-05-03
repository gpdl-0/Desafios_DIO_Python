MENU = """
   ## MENU DE OPERACOES BANCARIAS ##
        [d]-> Deposito
        [s]-> Saque
        [e]-> Extrato
        [f]-> Sair

Digite a opcao ==> """

LIMITE_SAQUE_DIARIO = 3
VALOR_LIMITE_POR_SAQUE = 500

saldo_usuario = 0
numero_saques_usuario = 0
id_transacao = 0

extrato = {}

while True:
    opcao_menu = str(input(MENU))

    if opcao_menu == "d":
        quantia_depositada = float(input('Digite quanto deseja depositar: '))

        if quantia_depositada <= 0:
            print("Valor invalido!")
        else:
            saldo_usuario += quantia_depositada
            id_transacao += 1
            extrato[f"Deposito (id{id_transacao})"] = f"R$ {quantia_depositada:.2f}"
            print('deposito realizado!')

    elif opcao_menu == "s":
        valor_saque = float(input("Digite o valor do saque: "))

        if saldo_usuario <= 0 or valor_saque > saldo_usuario:
            print("Saldo insuficiente!!")
        elif numero_saques_usuario > LIMITE_SAQUE_DIARIO:
            print("Limite de saque diario atingido!")
        elif valor_saque > VALOR_LIMITE_POR_SAQUE:
            print("Limite de R$500 por saque atingido!")
        else:
            saldo_usuario -= valor_saque
            numero_saques_usuario += 1
            id_transacao += 1
            extrato[f"Saque (id{id_transacao})"] = f"R$ {valor_saque:.2f}"
            print("Saque realizado!")

    elif opcao_menu == "e":
        if id_transacao is False:
            print("Nenhuma operacao realizada!")
        else:
            print(" ## EXTRATO ## \n",extrato)
            print(f"Saldo atual = R$ {saldo_usuario:.2f}")
            print("------------------------------------------")
        
    elif opcao_menu == "f":
        print("VOCE ESCOLHEU SAIR! >>>\nObrigado por utilizar este servico.")
        break
    
    else:
        print("Operacao invalida! Tente novamente.")


