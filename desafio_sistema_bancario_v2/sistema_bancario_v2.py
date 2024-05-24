
def menu():
    MENU = """
   ## MENU DE OPERACOES BANCARIAS ##
        [d]-> Deposito
        [s]-> Saque
        [e]-> Extrato
        [nc]-> Nova conta corrente
        [nu]-> Nono usuario
        [lc]-> Listar contas
        [f]-> Sair

Digite a opcao ==> """
    return str(input(MENU))

def depositar(saldo_usuario, quantia_depositada, extrato, /):

    if quantia_depositada > 0:
        saldo_usuario += quantia_depositada
        global id_transacao
        id_transacao += 1
        extrato[f"Deposito (id{id_transacao})"] = f"R$ {quantia_depositada:.2f}"
        print('deposito realizado!')
    else:
        print("Valor invalido!")

    return saldo_usuario, extrato

def sacar(*,saldo_usuario,valor_saque,extrato,limite, numero_saques,limite_saques):
    if saldo_usuario <= 0 or valor_saque > saldo_usuario:
        print("Saldo insuficiente!!")
    elif numero_saques > limite_saques:
        print("Limite de saque diario atingido!")
    elif valor_saque > limite:
        print("Limite de R$500 por saque atingido!")
    else:
        saldo_usuario -= valor_saque
        numero_saques += 1
        global id_transacao
        id_transacao += 1
        extrato[f"Saque (id{id_transacao})"] = f"R$ {valor_saque:.2f}"
        print("Saque realizado!")

    return saldo_usuario, extrato

def exibir_extrato(saldo, /, *,extrato):
    global id_transacao
    if id_transacao != 0:
        print(" ## EXTRATO ## \n",extrato)
        print(f"Saldo atual = R$ {saldo_usuario:.2f}")
        print("------------------------------------------")
        
    else:
        print("Nenhuma operacao realizada!")

def filtrar_usuario(cpf, usuarios):
    #Verifica em cada item da lista se o cpf fornecido ja existe
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # verifica se a lista e vazia e retorna sempre o primeiro elemento, ou seja unico CPF
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Ja existe usuario com este CPF! ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (RUA,N°,CIDADE,ESTADO)")
    usuarios.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(" $$$ Usuarios criado com sucesso! $$$ ")

def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nCONTA CRIADA COM SUCESSO!!!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n ### USUARIO N ENCONTRADO! OPERACAO CANCELADA! ### \n")

def listar_contas(contas):
    print("\n       $$$ Listagem de contas >>> ")
    for conta in contas:
        print(f"""
            Ag.: {conta['agencia']}
            C.C.: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """)
        print("-" * 30)


LIMITE_SAQUE_DIARIO = 3
VALOR_LIMITE_POR_SAQUE = 500
AGENCIA = "0001"

saldo_usuario = 0
numero_saques_usuario = 0
id_transacao = 0
extrato = {}

usuarios = []
contas = []
numero_conta = 0


while True:
    opcao_menu = menu()

    if opcao_menu == "d":
        valor_deposito = float(input("Informe o valor de deposito: "))

        saldo_usuario, extrato = depositar(saldo_usuario,valor_deposito,extrato)

    elif opcao_menu == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        saldo_usuario, extrato = sacar(saldo_usuario=saldo_usuario,valor_saque=valor_saque,extrato=extrato,limite=VALOR_LIMITE_POR_SAQUE,numero_saques=numero_saques_usuario,limite_saques=LIMITE_SAQUE_DIARIO)

    elif opcao_menu == "e":
        exibir_extrato(saldo_usuario,extrato=extrato)
        
    elif opcao_menu == "nu":
        criar_usuario(usuarios)

    elif opcao_menu == "nc":
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
            numero_conta += 1
    
    elif opcao_menu == "lc":
        listar_contas(contas)

    elif opcao_menu == "f":
        print("VOCE ESCOLHEU SAIR! >>>\nObrigado por utilizar este servico.")
        break

    else:
        print("Operacao invalida! Tente novamente.")
