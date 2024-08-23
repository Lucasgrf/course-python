# Projete um programa que simule as operações de um caixa eletrônico. Permite ao usuário fazer depósitos, saques e consultar saldo. 
# Use loops while para manter a interação até que o usuário decida sair.

saldo = 3000
while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        saldo += valor
        print("="*30)
        print("\nDepósito realizado com sucesso.")
        print(f"Saldo disponível: R$ {saldo:.2f} \n")
        print("="*30)
    elif opcao == 2:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= saldo:
            saldo -= valor
            print("="*30)
            print("\nSaque realizado com sucesso.")
            print(f"Saldo disponível: R$ {saldo:.2f} \n")
            print("="*30)
        else:
            print("="*30)
            print("\nSaldo insuficiente, saque não realizado.")
            print(f"Saldo disponível para saque: R$ {saldo:.2f} \n")
            print("="*30)
    elif opcao == 3:
        print("="*30)
        print(f"\nSaldo: R$ {saldo:.2f} \n")
        print("="*30)
    elif opcao == 4:
        print("="*30)
        print("Saindo...")
        print("="*30)
        break
    else:
        print("="*30)
        print("Opção inválida, tente novamente.")
        print("="*30)