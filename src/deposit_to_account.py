from edit_data import identify_client, update_clients_file, get_client_data
from operations import amount_input, increase_balance, update_balance
from utils import format_amount


def get_deposit_amount():
    amount = float(input('Por favor, digite o valor que deseja depositar: R$'))
    if(amount <= 0):
        print('Valor Inválido! Insira um valor positivo.')
        return get_deposit_amount()
    return amount


def deposit_to_account():
    try:
        client = identify_client(input("Digite o número da conta que deseja depositar: "))
        balance, account_number = get_client_data(
            client, ['balance', 'account_number'])
        print(f"\tSaldo atual: {format_amount(balance)}")
        update_balance(client, amount_input(
            get_deposit_amount), increase_balance)
    except:
        print(f'Operação cancelada.')
    else:
        print("\nSeu deposito foi efetuado com sucesso!\n")
