from edit_data import identify_client, update_clients_file, get_client_data


def get_deposit_amount():
    amount = int(input('Por favor, digite o valor que deseja depositar: '))
    if(amount <= 0):
        print('Valor Inválido, transação cancelada!')
        exit()
    return amount


def deposit_to_account():
    client = identify_client()
    balance, account_number = get_client_data(
        client, ['balance', 'account_number'])
    print(f"\tSaldo atual:  {balance}")

    updated_client_balance = int(balance) + get_deposit_amount()
    updated_client = [*client[0:5], updated_client_balance]
    update_clients_file(account_number, updated_client)

    print("\nSeu deposito foi efetuado com sucesso!\n")
