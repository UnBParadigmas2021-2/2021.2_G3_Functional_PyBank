from edit_data import identify_client, update_clients_file, get_client_data
from operations import decrease_balance, increase_balance, update_balance
from utils import format_amount
from withdraw_from_account import get_withdraw_amount


def transfer_to_account():
    client = identify_client()

    balance, account_number = get_client_data(
        client, ['balance', 'account_number'])
    print(f"\tSaldo atual: {format_amount(balance)}")

    print('Por favor, digite o valor que deseja transferir: ', end='')
    amount = get_withdraw_amount(balance)

    print(
        f'Para quem você deseja transferir a quantia de {format_amount(amount)}:?', end='')
    target = identify_client()

    update_balance(client, amount, decrease_balance)
    update_balance(target, amount, increase_balance)

    print("\nSua transferência foi efetuada com sucesso!\n")
