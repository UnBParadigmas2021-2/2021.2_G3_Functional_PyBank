from edit_data import get_client_data, identify_client, update_clients_file
from operations import amount_input, decrease_balance, update_balance
from utils import format_amount


def get_withdraw_amount(current_balance):
    def get_amount():
        amount = float(input('R$'))
        if(amount > float(current_balance)):
            print('Saldo insuficiente! Insira um valor menor.')
            return get_withdraw_amount(current_balance)
        return amount
    return amount_input(get_amount)


def withdraw_from_account():
    try:
        client = identify_client()
        balance, account_number = get_client_data(
            client, ['balance', 'account_number'])
        print(f"\tSaldo atual: {format_amount(balance)}")

        print('Por favor, digite o valor que deseja sacar: ', end='')
        update_balance(client, get_withdraw_amount(balance), decrease_balance)
    except:
        print(f'Operação cancelada.')
    else:
        print("\nSeu saque foi efetuado com sucesso!\n")
