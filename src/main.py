from edit_data import create_account, edit_client
from deposit_to_account import deposit_to_account
from transfer_to_account import transfer_to_account
from withdraw_from_account import withdraw_from_account


def main():
    print("############################")
    print("Escolha a operação desejada:")
    print("############################")
    print("1. Criar conta corrente")
    print("2. Criar conta poupança")
    print("3. Editar usuário")
    print("4. Depositar saldo")
    print("5. Transferir saldo")
    print("6. Consultar saldo")
    print("7. Sacar dinheiro")
    print("0. Sair")
    choice = int(input("Digite a escolha: "))

    if choice == 1:
        create_account("corrente")
    elif choice == 2:
        create_account("poupanca")
    elif choice == 3:
        edit_client()
    elif choice == 4:
        deposit_to_account()
        pass
    elif choice == 5:
        transfer_to_account()
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        withdraw_from_account()
        pass
    elif choice == 0:
        exit()
    else:
        print("Escolha inválida!")

    main()


if __name__ == "__main__":
    main()
