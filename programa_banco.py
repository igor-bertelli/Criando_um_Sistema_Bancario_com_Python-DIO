## Programa em python que simula um banco, com as funções de depositar, sacar e ver extrato.
# Autor Igor-bertelli

# Variáveis e constantes
saldo = 0
saque = 0
limite = 500
numero_saques = 3
LIM_SAQUES = 3 
OP_DEPOSITAR = 1 
OP_SAQUE = 2
OP_EXTRATO = 3
OP_SAIR = 4

# Menu
print("-------Bem vindo ao banco-------\n" )
print("Escolha uma opção")
print("1 - DEPOSITAR")
print("2 - SAQUE")
print("3 - EXTRATO")
print("4 - SAIR")

# Loop principal
while True:
    opcao = int(input("Digite a opção desejada: "))

    if opcao not in [OP_DEPOSITAR, OP_SAQUE, OP_EXTRATO, OP_SAIR]:
        print("Opção inválida! Escolha outra opção")
        continue

    if opcao == OP_DEPOSITAR:
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso")

        else:
            print("Opção inválida! Escolha outra opção")

    elif opcao == OP_SAQUE:
        valor = float(input("Digite o valor a ser sacado: "))

        if valor > 0:

            if valor > limite:
                print("Operação não realizada, o valor excedeu o limite de saque")

            elif numero_saques > LIM_SAQUES:
                print("Operação não realizada, o limite de saques foi atingido")

            elif valor > saldo:
                print("Operação não realizada, o valor excedeu o saldo")

            else:
                saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso")
                numero_saques += 1
        else:
            print("Opção inválida! Escolha outra opção")

    elif opcao == OP_EXTRATO:
        print("EXTRATO \n ")
        print(f"\nSaldo em R$ {saldo:.2f}")

    elif opcao == OP_SAIR:
        print("Saindo do programa...")
        break

