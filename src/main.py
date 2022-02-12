from edit_data import create_account, edit_client
from show_balance import show_user_balance 
def main():
    while(1):
        print("############################")
        print("Escolha a operação desejada:")
        print("############################")
        print("1. Criar conta corrente")
        print("2. Criar conta poupança")
        print("3. Editar usuário")
        print("4. Depositar saldo")
        print("5. Transferir saldo")
        print("6. Consultar saldo")
        print("0. Sair")
        choice = int(input("Digite a escolha: "))

        if choice == 1:
            create_account("corrente")
        elif choice == 2:
            create_account("poupanca")
        elif choice == 3:
            edit_client()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            show_user_balance()
            pass
        elif choice == 0:
            exit()
        else:
            print("Escolha inválida!")
            

if __name__ == "__main__":
    main()
