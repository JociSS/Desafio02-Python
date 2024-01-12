import textwrap
LIMITE_SAQUES = 3

def menu():
    menu_text = """
    [D]\tDepósito
    [S]\tSaque
    [E]\tExtrato
    [NC]\tNova conta
    [LC]\tListar Conta
    [NU]\tNovo Usuário
    [Q]\tSair
    """
    return input(textwrap.dedent(menu_text))
# any -> qualquer tipo/tipo não definido

def sacar(saldo: float, limite: float, numero_saque: int, extrato: str) -> tuple[float, int, str]:
    valor = float(input('Informe o valor do saque: '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= LIMITE_SAQUES
    novo_saldo = saldo
    novo_numero_saque = numero_saque
    
    if excedeu_saldo:
        print('Falha! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Falha! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('Falha! Você já atingiu o limite de saques hoje.')
    elif valor > 0:
        novo_saldo = saldo - valor
        extrato += f'Saque R$ {valor:.2f}\n'
        novo_numero_saque += 1
        print('Saque realizado com sucesso.')
    else:
        print('Erro: Valor de saque inválido. Tente novamente.')

    return novo_saldo, novo_numero_saque, extrato

def deposito(saldo: float, extrato: str) -> tuple[float, str]:
    valor = float(input('Informe o valor do depósito: '))
    
    if valor > 0:
        novo_saldo = saldo + valor
        extrato += f'Depósito R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso.')
    else:
        print('Erro: Valor de depósito inválido. Tente novamente.')

    return novo_saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n ============== Extrato ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo R$ {saldo:.2f}')
    print('===================================')

def criar_usuario(usuarios):
    cpf = input('Digite o CPF (Somente números): ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse CPF.')
        return

    nome = input('Digite nome completo: ')
    data_nascimento = input('Digite data de nascimento: ')
    endereco = input('Digite o endereço: ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('Usuário criado com sucesso!')

def filtra_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf_titular = input('Digite o CPF do titular da conta (Somente números): ')
    titular = filtra_usuario(cpf_titular, usuarios)

    if titular is None:
        print('Não existe usuário com esse CPF. Crie o usuário primeiro.')
        return contas

    saldo_inicial = float(input('Digite o saldo inicial da conta: '))
    limite_saque = float(input('Digite o limite de saque da conta: '))

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "titular": titular,
        "saldo": saldo_inicial,
        "limite_saque": limite_saque
    }

    contas.append(conta)
    print('Conta criada com sucesso!')

    return contas

def lista_conta(contas):
    if not contas:
        print('Não há contas cadastradas.')
        return

    print("\n ============== Lista de Contas ==============")
    for conta in contas:
        print(f"\nNúmero da Conta: {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Titular: {conta['titular']['nome']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print(f"Limite de Saque: R$ {conta['limite_saque']:.2f}")
        print('=============================================')

def main():

    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "S":
            saldo, numero_saque, extrato = sacar(saldo, limite, numero_saque, extrato)
        elif opcao == "E":
            exibir_extrato(saldo, extrato)
        
        elif opcao == 'D':
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == "NU":
            criar_usuario(usuarios)
        elif opcao == "NC":
            numero_conta = len(contas) + 1
            contas = criar_conta(AGENCIA, numero_conta, usuarios, contas)
        elif opcao == "LC":
            lista_conta(contas)
        elif opcao == "Q":
            break

if __name__ == "__main__":
    main()
