from edit_data import update_clients_file, get_client_data


def update_balance(client, amount: float, operation: callable):
    try:
        balance, account_number = get_client_data(
            client, ['balance', 'account_number'])
        updated_balance = operation(float(balance), float(amount))
        updated_client = [*client[0:5], updated_balance]
        update_clients_file(account_number, updated_client)
    except ValueError as error:
        print(f'{error}', end='')
        raise


def increase_balance(balance, amount: float):
    return float(balance) + float(amount)


def decrease_balance(balance, amount: float):
    if (balance < amount):
        raise ValueError('Saldo insuficiente! ')
    return float(balance) - float(amount)
